from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = m+n-1

        while i>=0 and j>= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        
        while j >= 0:
            ##case when [4,5,6], [1,2,3]
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here