def heap_sort(arr): # O(n log n)
    def heapify(arr, n, i): # O(log n)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[largest] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i) # n * O(log n) -> O(n log n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) # n * O(log n) -> O(n log n)

#        0  1  2   3   4  5  6   7  8   9   10  11 12  13
array = [5, 3, 21, 13, 1, 6, 15, 8, 33, 17, 18, 2, 19, 14]

print("Before: ", array)
heap_sort(array)
print("After: ", array)
