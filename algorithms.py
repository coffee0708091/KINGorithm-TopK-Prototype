import heapq
import random


def patient_key(patient: dict) -> tuple:
    """
    Higher risk_score is better.
    If risk_score is the same, higher id is used as a tie-breaker.
    """
    return (patient["risk_score"], patient["id"])


def full_sorting_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients by sorting all patients.
    Time Complexity: O(n log n)
    """

    sorted_patients = sorted(
        patients,
        key=patient_key,
        reverse=True
    )

    return sorted_patients[:k]


def heap_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients using a min-heap of size k.
    Time Complexity: O(n log k)
    """

    if k <= 0:
        return []

    heap = []

    for patient in patients:
        item = (patient["risk_score"], patient["id"], patient)

        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            if (item[0], item[1]) > (heap[0][0], heap[0][1]):
                heapq.heapreplace(heap, item)

    result = [item[2] for item in heap]

    # For display and validation consistency
    return sorted(result, key=patient_key, reverse=True)


def quickselect_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients using Quickselect.
    Average Time Complexity: O(n)
    Worst Time Complexity: O(n^2)

    Important:
    This function does NOT sort the final top-k result.
    It only selects the top-k patients.
    """

    if k <= 0:
        return []

    arr = patients[:]

    if k >= len(arr):
        return arr

    def is_greater(a: dict, b: dict) -> bool:
        return patient_key(a) > patient_key(b)

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_patient = arr[pivot_index]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left

        for i in range(left, right):
            if is_greater(arr[i], pivot_patient):
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left: int, right: int, target_index: int) -> None:
        while left <= right:
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == target_index:
                return
            elif pivot_index < target_index:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    select(0, len(arr) - 1, k - 1)

    # Return top-k only, without sorting.
    return arr[:k]