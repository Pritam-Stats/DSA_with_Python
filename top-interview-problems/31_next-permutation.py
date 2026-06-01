from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the point where there is a dip
        n = len(nums)
        dip = -1
        for i in range(n-1-1, -1, -1):
            if nums[i] < nums[i+1]:
                dip = i
                break

        if dip != -1:
            for i in range(n-1, dip, -1):
                if nums[i] > nums[dip]:
                    nums[i], nums[dip] = nums[dip], nums[i]
                    break

        # rev rest
        l, r = dip + 1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        return nums

# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
