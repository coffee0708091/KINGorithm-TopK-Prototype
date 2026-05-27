from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import time

from data_generator import generate_patients
from algorithms import full_sorting_top_k, heap_top_k, quickselect_top_k


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

current_patients = []


class GenerateRequest(BaseModel):
    n: int


class TopKRequest(BaseModel):
    ratio: float = 0.2
    repetitions: int = 5


@app.get("/")
def serve_index():
    return FileResponse("static/index.html")


@app.post("/generate")
def generate_data(request: GenerateRequest):
    global current_patients

    if request.n <= 0:
        return {"error": "n must be greater than 0"}

    current_patients = generate_patients(request.n)

    return {
        "message": "Patient data generated successfully",
        "count": len(current_patients),
        "patients": current_patients[:1000]
    }


def measure_average_time(func, patients: list[dict], k: int, repetitions: int):
    """
    Run an algorithm multiple times and return average execution time in ms.
    """

    total_time = 0
    last_result = None

    for _ in range(repetitions):
        start = time.perf_counter()
        last_result = func(patients, k)
        total_time += (time.perf_counter() - start) * 1000

    average_time = total_time / repetitions

    return last_result, average_time


@app.post("/top-k-risk")
def run_top_k_algorithms(request: TopKRequest):
    if not current_patients:
        return {"error": "No patient data. Please generate data first."}

    n = len(current_patients)
    k = max(1, int(n * request.ratio))
    repetitions = max(1, request.repetitions)

    sorting_result, sorting_time = measure_average_time(
        full_sorting_top_k,
        current_patients,
        k,
        repetitions
    )

    heap_result, heap_time = measure_average_time(
        heap_top_k,
        current_patients,
        k,
        repetitions
    )

    quickselect_result, quickselect_time = measure_average_time(
        quickselect_top_k,
        current_patients,
        k,
        repetitions
    )

    sorting_ids = {patient["id"] for patient in sorting_result}
    heap_ids = {patient["id"] for patient in heap_result}
    quickselect_ids = {patient["id"] for patient in quickselect_result}

    # Quickselect result is not sorted, so sort only the sample for display.
    sorted_top_sample = sorted(
        sorting_result[:20],
        key=lambda patient: (patient["risk_score"], patient["id"]),
        reverse=True
    )

    return {
        "n": n,
        "k": k,
        "ratio": request.ratio,
        "repetitions": repetitions,
        "execution_time_ms": {
            "full_sorting": round(sorting_time, 4),
            "heap_top_k": round(heap_time, 4),
            "quickselect": round(quickselect_time, 4)
        },
        "speedup_vs_sorting": {
            "heap_top_k": round(sorting_time / heap_time, 2) if heap_time > 0 else None,
            "quickselect": round(sorting_time / quickselect_time, 2) if quickselect_time > 0 else None
        },
        "validation": {
            "heap_matches_sorting": sorting_ids == heap_ids,
            "quickselect_matches_sorting": sorting_ids == quickselect_ids
        },
        "top_patients_sample": sorted_top_sample,
        "patients": current_patients[:1000],
        "selected_ids": list(sorting_ids)
    }