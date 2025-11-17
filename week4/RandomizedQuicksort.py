import random

def randomized_quicksort(nums):
    if not nums:
        return nums
        
    quicksort(nums, 0, len(nums) - 1)
    return nums

def quicksort(nums, low, high):
   
    if low >= high:
        return

    pivot_index = random.randint(low, high)
    
    pivot_val = nums[pivot_index]
    
    left= low     
    i = low      
    right = high    

    while i <= right:
        if nums[i] < pivot_val:
            nums[i], nums[left] =  nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] > pivot_val:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else: 
            i += 1
            
    quicksort(nums, low, left - 1)
    
    quicksort(nums, right + 1, high)


input1 = [2,5,3,3,-1,1]
print(f"Original array: {input1}")
randomized_quicksort(input1)
print(f"Sorted array:   {input1}")

   

   

    