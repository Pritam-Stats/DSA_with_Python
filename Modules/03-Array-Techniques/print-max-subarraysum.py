'''  
    Author: Pritam
''' 
'''  
Problem: print the subarray of the max subarray sum (extended kadane's) Dhruv Bhaiya 100x w12
Technique: kadane's
Intuition: track l and r as well
Mistake: 
Time: O(n)
Space: 
''' 
def maxSubArray(nums):
    n = len(nums)
    maxS = float("-inf")
    currSum = 0

    l = 0
    r = 0
    newStart = 0
    for i in range(n):
        currSum += nums[i]

        if currSum > maxS:
            maxS = currSum
            l = newStart
            r = i
            
        if currSum < 0:
            currSum = 0
            newStart = i+1

        

    return [maxS, nums[l:r+1]]
    

print(maxSubArray(nums=[-1]))
print(maxSubArray(nums=[5, 4, -1, 7, 8]))
print(maxSubArray(nums=[1]))
print(maxSubArray(nums= [-2, 1, -3,4,-1,2,1,-5,4]))