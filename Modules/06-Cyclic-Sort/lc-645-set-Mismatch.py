# one solution is with hashmap simple O(n), O(n)

## This is O(n), O(1)

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)

        i = 0
        while i < n:
            correctIdx = nums[i] - 1
            if nums[correctIdx] != nums[i]:
                nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
            else:
                i += 1

        for i in range(1, n+1):
            if i != nums[i-1]:
                return [nums[i-1], i]
