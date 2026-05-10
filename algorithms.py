import heapq
import random


def full_sorting_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients by sorting all patients.
    Time Complexity: O(n log n)
    """

    sorted_patients = sorted(
        patients,
        key=lambda patient: patient["risk_score"],
        reverse=True
    )

    return sorted_patients[:k]


def heap_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients using a min-heap of size k.
    Time Complexity: O(n log k)
    """

    heap = []

    for patient in patients:
        item = (patient["risk_score"], patient["id"], patient)

        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            if item[0] > heap[0][0]:
                heapq.heapreplace(heap, item)

    result = [item[2] for item in heap]

    return sorted(result, key=lambda patient: patient["risk_score"], reverse=True)


def quickselect_top_k(patients: list[dict], k: int) -> list[dict]:
    """
    Select top-k patients using Quickselect.
    Average Time Complexity: O(n)
    Worst Time Complexity: O(n^2)
    """

    arr = patients[:]

    def partition(left: int, right: int, pivot_index: int) -> int:
        pivot_score = arr[pivot_index]["risk_score"]

        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left

        for i in range(left, right):
            if arr[i]["risk_score"] > pivot_score:
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

    if k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr, key=lambda patient: patient["risk_score"], reverse=True)

    select(0, len(arr) - 1, k - 1)

    result = arr[:k]

    return sorted(result, key=lambda patient: patient["risk_score"], reverse=True)