

'''
    Author: Pritam
    Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
'''

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        i = 1
        while i<=n:
            correctIdx = nums[i-1] -1

            if nums[correctIdx] != nums[i-1]:
                #swap
                nums[correctIdx], nums[i-1] = nums[i-1], nums[correctIdx]

            else:
                i += 1

        for i in range(1, n+1):
            if nums[i-1] != i:
                ans.append(i)
        return ans



