import random 

def recursive_Binary_Search(arr, target, low, high ): 
   
    if high == low: # check for end of search 
        if arr[high] == target:  
            return high # == low 
        else: 
            return -1 # not found 
    else: 
        mid = (high + low) // 2 # calc mid using floor ex. 7//2 -> 3
        
        if arr[mid] == target: # target found 
            return mid 
        elif arr[mid] > target: 
            # need to go lower 
            high = mid - 1 # change the high value 
            return recursive_Binary_Search(arr,target,low,high) 
        else: 
            # need to go higher
            low = mid +1 # change the low value 
            return recursive_Binary_Search(arr,target,low,high) 



# array to test
arr = [1,2,3,4,5,6,7,8,9,10,12,14,16,17,20] 
low = 0 # initialize low to 0 
high = len(arr) - 1 # initialize high to max index 

# for loop that checks for all numbers in the array 
for i in arr: 
    # i = random.randint(1,100) # Uncomment this line to look for random integers in the sequence 
    idx = recursive_Binary_Search(arr, i,low, high) # function call 
    if idx == -1: 
        print('Target: ',i,' not found in sequence')
    else: 
        print('Target: ',i,' was found at index: ', idx)