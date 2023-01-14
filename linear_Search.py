def linear_Search(arr,target): 
    counter = 0 # keep track of idx
    for i in arr: # go through every position in array 
        if i == target: 
            return counter
        else: 
            counter += 1
    return -1 # not found


arr = [1,2,4,7,9,10] # array 
target = 4 # target we want to know the idx of 
idx = linear_Search(arr,target) # function call 
if idx == -1: 
    print('Target:',target,'was not found in sequence')
else: 
    print('Target:',target,'was found at index: ', idx)