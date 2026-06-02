from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, m, r = 0, 0, n-1
        while m<=r:
            if nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            elif nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            else:
                m += 1
        


        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here