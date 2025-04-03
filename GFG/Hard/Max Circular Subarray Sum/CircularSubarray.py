def circularSubarraySum(arr):
    ##Your code here
    maxSum = float('-inf')
    minSum = float('+inf')
    n = len(arr)
    currSum = 0
    totalSum = 0
    circularSum = 0
    currMin = 0
    
    #kadane
    for i in range(n):
        currSum += arr[i]
        currMin += arr[i]
        maxSum = max(maxSum, currSum)
        minSum = min(minSum, currMin)
        
        if currSum < 0:
            currSum = 0
            
        if currMin > 0:
            currMin = 0 #kadanes for min subarray sum
        
        
        totalSum += arr[i]

        
    circularSum = totalSum - minSum #in case of all negatives, this can become 0
    
    if maxSum < 0:  #we must check for the case when all are negatives
        return maxSum
        
    return max(circularSum, maxSum)

print(circularSubarraySum(arr = [5, -3, 5]))    #10
print(circularSubarraySum([8, -4, 3, -5, 4]))  # Expected: 12
print(circularSubarraySum([5, -2, 3, 4]))      # Expected: 10
print(circularSubarraySum([-1, -2, -3, -4]))   # Expected: -1 (all negatives)
print(circularSubarraySum([1, 2, 3, 4, 5]))    # Expected: 15 (all positives)
print(circularSubarraySum([-3, 4, -1, 5, -6])) # Expected: 8

# TC = O(N)
# SC = O(1)