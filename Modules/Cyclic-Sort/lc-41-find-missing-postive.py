
'''
    Author: Pritam
    Link: https://leetcode.com/problems/first-missing-positive/submissions/1971411912/
'''

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
            else:
                correctIdx = nums[i] -1
                if nums[correctIdx] != nums[i]:
                    nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
                else:
                    i += 1

        i = 0
        while i < n:
            if nums[i] != i+1:
                return i+1
            else:
                i += 1
        return n+1




