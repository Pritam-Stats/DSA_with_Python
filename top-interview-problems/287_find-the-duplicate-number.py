from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''easiest approach - Sort the array
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        '''


  ##  Floyd's tortoise and Hare Algorithm


        #two pointers
        slow = nums[0]  #will move 1 step
        fast = nums[0] #will move 2 step

        while True:
            slow = nums[slow]   #1 STEP
            fast = nums[nums[fast]] # 2 STEP

            if slow == fast:
                break

        ## phase 2
        # reinitialize slow and move both at same speed 1 step
        # keeping fast at the collision point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here