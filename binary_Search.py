# without recursion 

def binary_Search(arr,target):
    done = False  
    low = 0 # first idx
    high = len(arr) - 1 # last idx
    while done == False: 
        if high == low: 
            if arr[high] == target: 
                return high # = low 
            else:
                return -1 # not found 
        else: 
            mid = (high + low) // 2 # floor division for midpoint 
            if arr[mid] == target: 
                return mid 
            elif arr[mid] > target: 
                #too high 
                high = mid -1
            else: 
                # too low 
                low = mid + 1




# array to test
arr = [1,2,3,4,5,6,7,8,9,10,12,14,16,17,20] 
target = 17 # target 
idx = binary_Search(arr,target) # function call 
if idx == -1: 
    print('Target:',target,'was not found')
else: 
    print('Target:',target,'was found at index:',idx)
