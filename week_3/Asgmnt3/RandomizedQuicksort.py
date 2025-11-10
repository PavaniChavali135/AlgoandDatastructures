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


if __name__ == "__main__":
    

    # Normal case with repeated elements
    input1 = [10, 7, 8, 3, 3, 5, 3, 3]
    print(f"\nOriginal array: {input1}")
    randomized_quicksort(input1)
    print(f"Sorted array:   {input1}")

    #Empty array
    input2 = []
    print(f"\nOriginal (empty): {input2}")
    randomized_quicksort(input2)
    print(f"Sorted (empty):   {input2}")

    # Already sorted array
    input3 = [1, 2, 3, 4, 5, 6, 7]
    print(f"\nOriginal array: {input3}")
    randomized_quicksort(input3)
    print(f"Sorted array:   {input3}")

    # Reverse sorted array
    input4 = [7, 6, 5, 4, 3, 2, 1]
    print(f"\nOriginal array: {input4}")
    randomized_quicksort(input4)
    print(f"Sorted array:   {input4}")

   

    