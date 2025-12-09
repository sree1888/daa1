import random
import time
import heapq

# ------------------------ Generate random data ------------------------
data = [random.randint(1, 500) for _ in range(50)]
print("Original Data:\n", data)
print("\n==============================\n")

# ------------------------ Sorting Algorithms ------------------------
def bubble_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def heap_sort(arr):
    a = arr[:]
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

def bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = (max_val - min_val)//bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = (num - min_val)//bucket_size
        buckets[index].append(num)
    sorted_list = []
    for b in buckets:
        sorted_list.extend(sorted(b))
    return sorted_list

# ------------------------ Test and Compare ------------------------
def test_sort(name, func, data):
    start = time.perf_counter()
    sorted_data = func(data)
    end = time.perf_counter()
    print(f"{name} Sorted Data:\n{sorted_data}")
    print(f"{name} Time: {end-start:.6f} seconds\n")
    return end-start, sorted_data

results = {}
results["Bubble Sort"] = test_sort("Bubble Sort", bubble_sort, data)
results["Insertion Sort"] = test_sort("Insertion Sort", insertion_sort, data)
results["Selection Sort"] = test_sort("Selection Sort", selection_sort, data)
results["Heap Sort"] = test_sort("Heap Sort", heap_sort, data)
results["Bucket Sort"] = test_sort("Bucket Sort", bucket_sort, data)

# ------------------------ Find Best Algorithm ------------------------
best_algo = min(results, key=lambda x: results[x][0])
best_time = results[best_algo][0]
best_sorted = results[best_algo][1]

print("==============================")
print(f"Fastest Algorithm: {best_algo}")
print(f"Execution Time   : {best_time:.6f} seconds")
print("Sorted Data from Fastest Algorithm:")
print(best_sorted)
print("==============================")
