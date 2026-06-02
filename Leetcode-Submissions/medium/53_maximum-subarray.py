from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        for x in nums:
            if cur < 0:
                cur = 0
            cur += x
            ans = max(ans, cur)
        return ans

        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here