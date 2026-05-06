#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution(object):
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerSet = []
        n = len(nums)
        ## there are 2^n possible subsets
        for mask in range(1<<n):
            ##think of it like a binary running from 000 to 111
            #this is how we can add all nums act as a switch which one to include
            subset = []
            for i in range(n):
                if mask&(1<<i):
                    #if on
                    subset.append(nums[i])
            powerSet.append(subset)
        return powerSet


        
# @lc code=end

