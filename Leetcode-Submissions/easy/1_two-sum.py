from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}

        for i, x in enumerate(nums):
            comp = target - x
            if comp in seen:
                return [seen[comp], i]
            seen[x] = i
    ## TC: O(n)
    ## SC: O(n)

# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
