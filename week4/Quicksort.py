def pivot(arr, left , right):
    pivot = arr[left] # pivot as first element
    start = left
    end = right

    while start<end:
            while start<=right and arr[start] <= pivot:
                start = start+1
            while end>=left and  arr[end] > pivot:
                 end = end-1
            
            if start<end:
                arr[start],arr[end] = arr[end],arr[start]
    
    arr[left], arr[end] = arr[end], arr[left]
    return end

def partition(arr, left , right):
     #partitiong the array
    if left<right:
         loc = pivot(arr,left,right)
         
         # recursively sort the left subarray
         partition(arr,left, loc-1)
         
         # recursively sort the right subarray
         partition(arr, loc+1, right)



arr = [2,5,3,3,-1,1]

print(f"original array: {arr}")

partition(arr,0,len(arr)-1)
print(f"sorted array: {arr}")


    