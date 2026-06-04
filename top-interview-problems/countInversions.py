'''
## Count Inversions

Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.
Example 1
Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5

Explanation:

The responsible indexes are:
nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5
Example 2
Input: nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation:
nums is sorted, hence no inversions present.
'''


# ================================
# Author: Pritam
# ================================

class Solution:
    def numberOfInversions(self, nums):
        ##easy approach - O(n2)

        ## Later TODO - Merge Sort
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n): ## j > i
                if nums[i] > nums[j]:
                    cnt += 1
        return cnt

