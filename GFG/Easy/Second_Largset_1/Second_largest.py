# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735


# Brute Force Approach



# Better Solution



# Optimal solution
def getSecondLargest(arr):  
    # Code Here
    n = len(arr)
    
    #need to initialize both 2nd largest and the largest
    largest = arr[0]
    slargest = -1   #the default if no second largest exist
    
    # loop through every value, check for the largest, if largest changes.. second largest will change simultaneously
    for i in range(1, n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
            
        # need to check the case where largest won't change but second largest might be
        elif (arr[i] < largest and arr[i] > slargest):
            slargest = arr[i]
            
    return slargest

print(getSecondLargest(arr=[10, 5, 10]))
print(getSecondLargest(arr=[10, 10, 10]))