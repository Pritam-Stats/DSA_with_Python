
def maxSubArray(nums: list[int]) -> int:
    n = len(nums)
    currSum = 0
    maxSum = float('-inf')  #this will handle the case of all negatives
    for i in range(n):
        currSum += nums[i]
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    return maxSum

print(maxSubArray(nums= [-1]))
print(maxSubArray(nums= [5,4,-1,7,8]))
print(maxSubArray(nums= [1]))
print(maxSubArray(nums= [-2,1,-3,4,-1,2,1,-5,4]))