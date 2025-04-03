def maxSubarraySumCircular(nums: list[int]) -> int:
    n = len(nums)
    maxSum = float('-inf')
    minSum = float('+inf')
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    circularSum = 0
    for i in range(n):
        currMaxSum += nums[i]
        currMinSum += nums[i]
        maxSum = max(currMaxSum, maxSum)
        minSum = min(currMinSum, minSum)
        if currMaxSum < 0:
            currMaxSum = 0
        if currMinSum > 0:
            currMinSum = 0
        totalSum += nums[i]
    circularSum = totalSum - minSum
    if maxSum < 0:
        return maxSum
    return max(maxSum, circularSum)


print(maxSubarraySumCircular([1,-2,3,-2]))   # Expected: 3
print(maxSubarraySumCircular([5,-3,5]))      # Expected: 10
print(maxSubarraySumCircular([-3,-2,-3]))    # Expected: -2
print(maxSubarraySumCircular([3, -1, 2, -1])) # Expected: 4
print(maxSubarraySumCircular([8, -4, 3, -5, 4])) # Expected: 12


