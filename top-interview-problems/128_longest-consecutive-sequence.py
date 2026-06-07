from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        numSet = set(nums)
        for x in numSet:
            if x-1 not in numSet:
                curr = x
                streak = 1

                while curr+1 in numSet:
                    streak += 1
                    curr += 1
                longest = max(longest, streak)
        return longest
    
    ## TC: O(n)
    ## SC: O(n)
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here