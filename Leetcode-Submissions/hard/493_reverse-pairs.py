from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #brute
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > 2* nums[j]:
                    cnt += 1
        return cnt

    ##TLE. Need to learn Merge Sort. Merge Sort Approach needed
    ## TC: O(n2)
    ## SC: O(1)

        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here