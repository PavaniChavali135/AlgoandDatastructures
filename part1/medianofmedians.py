import math

def partition(nums, low, high, pivot_value):
    i = low
    while i <= high and nums[i] != pivot_value:
        i += 1
    
    nums[i], nums[high] = nums[high], nums[i]
    
    pivot = nums[high]
    i = low - 1
    
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def median(elements):
    elements.sort()
    mid = elements[len(elements) // 2]
    return mid

def selection(arr, k, low=None, high=None):
    if low is None: 
        low = 0
    if high is None: 
        high = len(arr) - 1

    if low == high:
        return arr[low]

    n = high - low + 1
    medians = []
    
    for i in range(0, n, 5):
        leftarray = low + i
        rightarray = min(low + i + 4, high)
        
        arrayelements = arr[leftarray : rightarray + 1]
        medians.append(median(arrayelements))
    

    position = (len(medians) + 1) // 2
    pivot = selection(medians.copy(), position) 
    actualpivot = partition(arr, low, high, pivot)
    pivotpos = actualpivot - low + 1

    if k == pivotpos:
        return arr[actualpivot]
    elif k < pivotpos:
        return selection(arr, k, low, actualpivot - 1)
    else:
        newk = k - pivotpos
        return selection(arr, newk, actualpivot + 1, high)

givennk = 5
nums = [100, 16, 92, 84, 72, 66]
res = selection(nums.copy(), givennk)
print(f"{res} is the {givennk}th smallest element")