from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start


# ================================
# Author: Pritam
# ================================

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ## binary search
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        
        low, high = 1, n-2

        while low <= high:
            # mid = low + ((high - low)//2) 
            mid = low + ((high - low)>>2) 
            if nums[mid + 1] > nums[mid]:
                low = mid + 1
            elif nums[mid - 1] > nums[mid]:
                high = mid -1
            else:
                return mid
    ## TC: O(log n)
    ## SC: O(1)
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here