import random 

def recursive_Binary_Search(arr, target, low, high ): 
   
    if high == low: 
        if arr[high] == target:  
            return high 
        else: 
            return -1
    else: 
        mid = (high + low) // 2 
        
        if arr[mid] == target: 
            return mid 
        elif arr[mid] > target: 
            # need to go lower 
            return recursive_Binary_Search(arr,target,low,mid-1)
        else: 
            # need to go higher
            return recursive_Binary_Search(arr,target,mid+1,high)



arr = [1,2,3,4,5,6,7,8,9,10,12,14,16,17] 
low = 0 
high = len(arr) - 1
for i in arr: 
    i = random.randint(1,100)
    idx = recursive_Binary_Search(arr, i,low, high)
    if idx == -1: 
        print('Target: ',i,' not found in sequence')
    else: 
        print('Target: ',i,' was found at index: ', idx)