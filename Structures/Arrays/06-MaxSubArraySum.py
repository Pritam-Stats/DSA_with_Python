"""_summary_
Kadane's Algorithm
LC 53.
Make the problem simpler
Bring the Time from O(N2) to O(N)
"""

def maxSubSumKadanesAlgo(arr):
    n = len(arr)
    currSum, maxSum = 0, float("-inf")
    for i in range(n):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    return maxSum



##---------------------------------------------------------------------------------

## Brute Force Approach
## store the sums of all the possible subarrays and return the max
def maxSubSumBF(arr):
    subSums = []
    n = len(arr)
    for st in range(n):
        for end in range(st, n):
            currSum = 0
            for i in range(st, end+1):
                currSum += arr[i]
            # subSums.append(sum(arr[st:end+1]))
            subSums.append(currSum)
    return max(subSums)

arr = [1,2,3,-4,-1]
# the total possible subarray is n*n+1/2 = 10


def maxSubSumBF2(arr):
    subSums = []
    maxSum = float("-inf")
    n = len(arr)
    for st in range(n):
        currSum = 0 #at every start point we are initializing a currsum
        for end in range(st, n):
            currSum += arr[end]     ## we are adding 1 element and comparing at that step
            maxSum = max(maxSum, currSum)

    return maxSum




        
arr = [-1, 2, -1,-2,-2,-1]
print(maxSubSumBF(arr))
print(maxSubSumBF2(arr))
print(maxSubSumKadanesAlgo(arr))

    
# def maxSubSumOp(arr):
