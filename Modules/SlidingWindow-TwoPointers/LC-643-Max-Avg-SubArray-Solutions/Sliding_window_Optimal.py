'''  
    Author: Pritam
''' 
'''  
Problem: max sub array avg
Technique: sliding window
Intuition: fixed len
Mistake: Not handling the case when all are neg or max will be neg so initialize maxS with -inf is imp
Time: O(N)
Space: O(1)
''' 
class Solution:  # 26th march 2026
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        '''
            Author: Pritam
        '''
        # sliding window
        n = len(nums)
        maxS = float("-inf")    # 0 fails for all negatives
        runningSum = 0
        if len(nums) == 1:
            return nums[0] * 1.0

        # first k
        for i in range(k):
            runningSum += nums[i]
        maxS = max(maxS, runningSum)

        for i in range(k, n):
            runningSum += nums[i]
            runningSum -= nums[i-k]
            maxS = max(maxS, runningSum)

        return maxS/k








def findMaxAverage(nums: list[int], k: int) -> float:
    # sliding window    #25th april 2025
    window_sum = sum(nums[:k])
    max_sum = window_sum
    #slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k] #ultimately there will remain the sum k elements each time
        max_sum = max(window_sum, max_sum)
    return max_sum/k
        
print(findMaxAverage(nums=[5], k=1))    #5
print(findMaxAverage(nums=[1,12,-5,-6,50,3], k=4))    #12.75

#O(N)