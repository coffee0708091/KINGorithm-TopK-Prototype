import random


def calculate_risk_score(patient: dict) -> float:
    """
    Calculate a simple medical cost risk score.
    Score range is roughly 0 ~ 100.
    """

    age_score = min(patient["age"] / 100, 1.0)
    visit_score = min(patient["visit_count"] / 50, 1.0)
    chronic_score = min(patient["chronic_disease_count"] / 5, 1.0)
    cost_score = min(patient["previous_medical_cost"] / 10_000_000, 1.0)
    admission_score = min(patient["admission_count"] / 10, 1.0)

    risk_score = (
        0.30 * cost_score
        + 0.25 * visit_score
        + 0.20 * chronic_score
        + 0.15 * age_score
        + 0.10 * admission_score
    ) * 100

    return round(risk_score, 2)


def generate_patients(n: int) -> list[dict]:
    """
    Generate random patient records.
    """

    patients = []

    for i in range(1, n + 1):
        patient = {
            "id": i,
            "age": random.randint(18, 90),
            "gender": random.choice(["M", "F"]),
            "visit_count": random.randint(0, 60),
            "chronic_disease_count": random.randint(0, 6),
            "previous_medical_cost": random.randint(100_000, 15_000_000),
            "admission_count": random.randint(0, 12),
        }

        patient["risk_score"] = calculate_risk_score(patient)
        patients.append(patient)

    return patients