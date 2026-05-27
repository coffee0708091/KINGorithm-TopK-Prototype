let latestPatients = [];
let latestSelectedIds = new Set();

const generateBtn = document.getElementById("generateBtn");
const runBtn = document.getElementById("runBtn");
const patientCountInput = document.getElementById("patientCount");
const resultTable = document.getElementById("resultTable");
const validationBox = document.getElementById("validationBox");
const patientList = document.getElementById("patientList");
const canvas = document.getElementById("riskCanvas");
const ctx = canvas.getContext("2d");

generateBtn.addEventListener("click", generatePatients);
runBtn.addEventListener("click", runAlgorithms);

async function generatePatients() {
    const n = Number(patientCountInput.value);

    const response = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ n })
    });

    const data = await response.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    latestPatients = data.patients || [];
    latestSelectedIds = new Set();

    resultTable.innerHTML = `
        <tr>
            <td colspan="3">${data.count} patients generated. Click "Run Algorithms".</td>
        </tr>
    `;

    validationBox.textContent = "";
    patientList.innerHTML = "";
    drawCanvas(latestPatients, latestSelectedIds);
}

async function runAlgorithms() {
    const response = await fetch("/top-k-risk", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ratio: 0.2 })
    });

    const data = await response.json();

    if (data.error) {
        alert(data.error);
        return;
    }

    latestPatients = data.patients || [];
    latestSelectedIds = new Set(data.selected_ids || []);

    renderResultTable(data);
    renderValidation(data);
    renderTopPatients(data.top_patients_sample || []);
    drawCanvas(latestPatients, latestSelectedIds);
}

function renderResultTable(data) {
    const times = data.execution_time_ms;
    const speedup = data.speedup_vs_sorting;

    resultTable.innerHTML = `
        <tr>
            <td>Full Sorting</td>
            <td>${times.full_sorting}</td>
            <td>1.00x</td>
        </tr>
        <tr>
            <td>Min-Heap Top-K</td>
            <td>${times.heap_top_k}</td>
            <td>${speedup.heap_top_k}x</td>
        </tr>
        <tr>
            <td>Quickselect</td>
            <td>${times.quickselect}</td>
            <td>${speedup.quickselect}x</td>
        </tr>
    `;
}

function renderValidation(data) {
    const heapOk = data.validation.heap_matches_sorting;
    const quickOk = data.validation.quickselect_matches_sorting;

    validationBox.innerHTML = `
        Patients: ${data.n} / Top-K: ${data.k}<br>
        Heap result matches sorting: ${heapOk ? "✅ true" : "❌ false"}<br>
        Quickselect result matches sorting: ${quickOk ? "✅ true" : "❌ false"}
    `;
}

function renderTopPatients(patients) {
    patientList.innerHTML = "";

    patients.forEach(patient => {
        const div = document.createElement("div");
        div.className = "patient-card";

        div.innerHTML = `
            <strong>ID ${patient.id}</strong> /
            Risk Score: ${patient.risk_score} /
            Age: ${patient.age} /
            Visits: ${patient.visit_count} /
            Previous Cost: ${patient.previous_medical_cost.toLocaleString()} KRW
        `;

        patientList.appendChild(div);
    });
}

function drawCanvas(patients, selectedIds) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!patients || patients.length === 0) {
        ctx.fillText("No patient data", 30, 30);
        return;
    }

    const padding = 50;

    const maxCost = Math.max(...patients.map(p => p.previous_medical_cost));
    const maxRisk = Math.max(...patients.map(p => p.risk_score));

    drawAxes(padding);

    patients.forEach(patient => {
        const x = padding + (patient.previous_medical_cost / maxCost) * (canvas.width - padding * 2);
        const y = canvas.height - padding - (patient.risk_score / maxRisk) * (canvas.height - padding * 2);

        if (selectedIds.has(patient.id)) {
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2);
            ctx.fill();
        } else {
            ctx.beginPath();
            ctx.arc(x, y, 2, 0, Math.PI * 2);
            ctx.fill();
        }
    });
}

function drawAxes(padding) {
    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, canvas.height - padding);
    ctx.lineTo(canvas.width - padding, canvas.height - padding);
    ctx.stroke();

    ctx.fillText("Risk Score", 10, padding - 10);
    ctx.fillText("Previous Medical Cost", canvas.width - 190, canvas.height - 15);
}