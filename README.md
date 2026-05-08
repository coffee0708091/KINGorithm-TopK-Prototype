<div align="center">

# 🩺 KINGorithm

### Medical Cost Risk Top-K Selection Algorithm Web App

**고비용 의료비 위험군 선별을 위한 Top-K 알고리즘 비교 웹 서비스**

</div>

---

## 📌 Project Summary

KINGorithm is an **algorithm-focused web application** that selects the top 20% high-risk patients based on medical cost risk scores.

This project is designed for an **Algorithm course**, so the main focus is not AI prediction itself, but the comparison of different **Top-K selection algorithms**.

> Given `n` patient records with risk scores,  
> select the top `k` patients with the highest risk scores.

In this project:

```text
k = top 20% of all patients
```

The selected patients are classified as the **high-risk group**.

---

## 🎯 Core Idea

Medical cost prediction is useful, but in real-world healthcare and insurance scenarios, it is often more important to identify high-risk patients early.

Therefore, this project converts the medical risk problem into an algorithmic problem:

> **How can we efficiently select the highest-risk patients from a large dataset?**

---

## 🧠 Algorithms Compared

| Approach | Description | Time Complexity |
|---|---|---|
| **Full Sorting** | Sort all patients by risk score and select top k | `O(n log n)` |
| **Min-Heap Top-K** | Maintain a heap of size k while scanning all patients | `O(n log k)` |
| **Quickselect** | Use partition-based selection to find the k-th highest score | Average `O(n)`, Worst `O(n²)` |

---

## 🧩 Main Features

- Generate random patient records
- Calculate medical cost risk scores
- Select the top 20% high-risk patients
- Run and compare multiple Top-K algorithms
- Measure execution time for each algorithm
- Display speedup ratio
- Visualize patient risk distribution on a 2D canvas
- Highlight selected high-risk patients
- Optionally generate natural language explanations using an LLM

---

## 🏥 Patient Data

Each generated patient record contains:

| Feature | Description |
|---|---|
| **Age** | Patient age |
| **Gender** | Patient gender |
| **Visit Count** | Number of hospital visits |
| **Chronic Disease Count** | Number of chronic diseases |
| **Previous Medical Cost** | Medical cost from the previous year |
| **Admission Count** | Number of hospital admissions |
| **Risk Score** | Calculated medical cost risk score |

---

## 📊 Risk Score Calculation

A simple weighted scoring formula is used to calculate each patient’s risk score.

```text
risk_score =
0.30 * previous_cost_score
+ 0.25 * visit_count_score
+ 0.20 * chronic_disease_score
+ 0.15 * age_score
+ 0.10 * admission_score
```

The calculated `risk_score` is used as the key value for Top-K selection.

---

## 🏗️ System Architecture

```text
[Frontend]
- User input
- Canvas visualization
- Result table

        ↓

[Backend]
- Patient data generation
- Risk score calculation
- Algorithm execution
- Execution time measurement

        ↓

[Top-K Algorithms]
- Full Sorting
- Min-Heap Top-K
- Quickselect

        ↓

[Optional LLM Module]
- Natural language explanation
- Risk report generation
```

---

## 🖥️ Web Interface

The web application will provide:

| UI Component | Description |
|---|---|
| **Patient Count Input** | User chooses the number of patients |
| **Generate Button** | Generates random patient data |
| **Run Algorithms Button** | Executes all Top-K algorithms |
| **Result Table** | Shows execution time and speedup |
| **2D Canvas** | Visualizes patient risk distribution |
| **Highlighted Points** | Displays selected high-risk patients |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serve the frontend page |
| `POST` | `/generate` | Generate random patient records |
| `POST` | `/top-k-risk` | Run Top-K algorithms and return results |
| `POST` | `/explain` | Optional LLM-based explanation |

---

## 🛠️ Tech Stack

| Part | Technology |
|---|---|
| **Frontend** | HTML, CSS, JavaScript, Canvas |
| **Backend** | Python, FastAPI or Flask |
| **Algorithms** | Python |
| **Data Processing** | Pandas / Python standard library |
| **Optional LLM** | Upstage Solar |
| **Version Control** | GitHub |

---

## 📁 Project Structure

```text
KINGorithm/
├── app.py
├── algorithms.py
├── data_generator.py
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── style.css
    └── app.js
```

---

## 📈 Performance Evaluation

The final report will compare execution time using different input sizes.

| Number of Patients | Full Sorting | Min-Heap Top-K | Quickselect |
|---:|---:|---:|---:|
| 100 | - | - | - |
| 1,000 | - | - | - |
| 5,000 | - | - | - |

The report will analyze why Top-K algorithms can be more efficient than full sorting when only the highest-risk group is needed.

---

## 📄 Report Focus

The final report will focus on the following points:

1. Defining the medical risk selection task as a Top-K selection problem
2. Explaining each algorithm and its time complexity
3. Comparing execution time for different input sizes
4. Visualizing the selected high-risk group
5. Analyzing why selecting only the top k elements can be more efficient than sorting all elements
6. Explaining the role of the optional LLM module as a result explanation tool

---

## 👥 Team Roles

| Role | Member |
|---|---|
| **Frontend Lead** | 황유림 |
| **Backend / Server Lead** | 고은서 |
| **LLM Integration / Prompt Engineering Lead** | 이유라 |
| **PM / Planning / Documentation / Presentation Coordination** | 박재형 |

---

## ⚠️ Project Focus

Although this project uses a medical cost risk scenario, the core contribution is **algorithmic comparison**.

The LLM is **not** the main algorithm.

It is used only as an optional explanation module after the Top-K selection algorithms produce their results.

> **Main Focus:**  
> Top-K selection, time complexity comparison, execution time analysis, and visualization.

---

<div align="center">

### KINGorithm  
**Selecting high-risk patients through algorithmic efficiency.**

</div>