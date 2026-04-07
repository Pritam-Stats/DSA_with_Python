'''
    Author: Pritam
    Problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 1
        while i<= n:
            correctIdx = nums[i-1] -1

            if nums[correctIdx] != nums[i-1]:
                nums[i-1], nums[correctIdx] = nums[correctIdx], nums[i-1]

            else:
                i += 1
        ans = []

        for i in range(1, n+1):
            if nums[i-1] != i:
                ans.append(nums[i-1])

        return ans


    def findDuplicatesNegMarking(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            idx = abs(nums[i]) -1
            if nums[idx] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[idx] *= -1
        return ans
        
