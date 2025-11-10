def heap_sort(arr):
    n = len(arr)

    max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def max_heap(arr):
    n = len(arr)
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    largest = i
    leftnode = 2 * i + 1
    rightnode = 2 * i + 2

    if leftnode < n and arr[leftnode] > arr[largest]:
        largest = leftnode

    if rightnode < n and arr[rightnode] > arr[largest]:
        largest = rightnode

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



inputlist = [12, 11, 13, 5, 6, 7, 30, -5, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
print(f"Original list: {inputlist}")
    
heap_sort(inputlist)
    
print(f"Sorted list:   {inputlist}")

   