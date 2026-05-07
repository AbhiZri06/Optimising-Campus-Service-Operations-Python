import time
import random
import matplotlib.pyplot as plt

#Selection Sort
def selection_sort(arr):
    a = arr.copy() #original data is not changed
    comparisons = 0

    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

    return a, comparisons


#Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    comparisons = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a, comparisons


#Linear Search
def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


#Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


#Process of sorting algorithms
data_sizes = [50, 100, 200, 400]

selection_times = []
insertion_times = []

selection_comps = []
insertion_comps = []

for n in data_sizes:
    data = [random.randint(1, 1000) for x in range(n)] #Random data sets

    #Selection Sort
    start = time.time()
    x, comps = selection_sort(data)
    end = time.time()
    selection_times.append(end - start)
    selection_comps.append(comps)

    #Insertion Sort
    start = time.time()
    x, comps = insertion_sort(data)
    end = time.time()
    insertion_times.append(end - start)
    insertion_comps.append(comps)

    #memory usage
    memory_used = len(data)
    print("Sorting | Size:", n, "| Memory used:", memory_used)


#Time Graphs of sorting algorithms
plt.plot(data_sizes, selection_times, label="Selection Sort")
plt.plot(data_sizes, insertion_times, label="Insertion Sort")
plt.xlabel("Number of elements")
plt.ylabel("Execution time (seconds)")
plt.title("Sorting Time Comparison")
plt.legend() #makes structure for the graph
plt.savefig("sorting time.png")
plt.show()

#Comparisons Graphs of sorting algorithms
plt.plot(data_sizes, selection_comps, label="Selection Sort")
plt.plot(data_sizes, insertion_comps, label="Insertion Sort")
plt.xlabel("Number of elements")
plt.ylabel("Number of comparisons")
plt.title("Sorting Comparison Count")
plt.legend()
plt.savefig("sorting comparisons.png")
plt.show()


#Process of searching algorithms
search_sizes = [100, 500, 1000, 2000]

linear_times = []
binary_times = []

linear_comps = []
binary_comps = []

for n in search_sizes:
    data = [random.randint(1, 5000) for x in range(n)]
    data.sort()  # required for binary search
    target = data[n // 2]

    #Linear Search
    start = time.time()
    x, comps = linear_search(data, target)
    end = time.time()
    linear_times.append(end - start)
    linear_comps.append(comps)

    #Binary Search
    start = time.time()
    x, comps = binary_search(data, target)
    end = time.time()
    binary_times.append(end - start)
    binary_comps.append(comps)

    print("Searching | Size:", n, "| Memory used:", len(data))


#Time graphs of searching algorithms
plt.plot(search_sizes, linear_times, label="Linear Search")
plt.plot(search_sizes, binary_times, label="Binary Search")
plt.xlabel("Number of elements")
plt.ylabel("Execution time (seconds)")
plt.title("Search Time Comparison")
plt.legend() 
plt.savefig("search time.png")
plt.show()

#Comparisons Graphs of searching algorithms
plt.plot(search_sizes, linear_comps, label="Linear Search")
plt.plot(search_sizes, binary_comps, label="Binary Search")
plt.xlabel("Number of elements")
plt.ylabel("Number of comparisons")
plt.title("Search Comparison Count")
plt.legend() #making squares for graphs
plt.savefig("search comparisons.png")
plt.show()

print("images are exported!")
