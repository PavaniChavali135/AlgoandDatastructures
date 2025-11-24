import random

def randompick(nums, k, low=None, high=None):
    if low is None: 
        low = 0
    if high is None: 
        high = len(nums) - 1
    if low == high:
        return nums[low]

    randompivot = random.randint(low, high)
    actualpivot = partition(nums, low, high, randompivot)
    pivotpos= actualpivot - low + 1
    
    if k == pivotpos:
        return nums[actualpivot]
    elif k < pivotpos:
        return randompick(nums, k, low, actualpivot - 1)
    else:
        newk = k - pivotpos
        return randompick(nums, newk, actualpivot + 1, high)


def partition(nums, low, high, pivot_index):
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


givennk = 5
nums = [100, 16, 92, 84, 72, 66]
res = randompick(nums.copy(), givennk)
print(f"{res} is the {givennk}th smallest element")