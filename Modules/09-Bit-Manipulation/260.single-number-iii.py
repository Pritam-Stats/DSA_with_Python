#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#




from typing import List
# @lc code=start
# ================================
# Author: Pritam
# ================================

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]: 
        xorRes = 0
        for x in nums:
            xorRes ^= x

        ## find the first setbit or any setbit position
        ## we can a run a loop and check setbit if found 1 return
        mask = xorRes&(-xorRes)    ##[x & -x return 2^i]    #only one setbit, first set of difference

        num1, num2 = 0, 0

        for x in nums:
            if x&mask:  #means 1 is there
                num1 ^= x
            else:
                #means 0 is there
                num2 ^= x
                

        ans = [num1, num2]

        return ans
    ## TC: O(n)
    ## SC: O(1)

# @lc code=end

