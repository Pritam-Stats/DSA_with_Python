'''
### Find the repeating and missing number

Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.

Example 1
Input: nums = [3, 5, 4, 1, 1]

Output: [1, 2]

Explanation:

1 appears two times in the array and 2 is missing from nums
'''

# ================================
# Author: Pritam
# ================================


class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        ## one approach is frequency

        ## Math Approach
        sn = n*(n+1)//2
        sn2 = n*(n+1)*(2*n + 1)//6

        ## actual sums
        s = 0
        s2 = 0

        for x in nums:
            s += x
            s2 += x**2

        ##diffs
        d1 = sn - s #(x-y)
        d2 = sn2 - s2 #x^2 - y^2

        ## x+y 
        x_plus_y = d2//d1

        x = (d1 + x_plus_y)//2
        y = x_plus_y - x

        return [x, y]

