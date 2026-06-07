from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue    #skip

            for j in range(i+1, n):
                if j >i+1 and nums[j] == nums[j-1]:
                    continue

                ## step 3 tp
                l, r = j+1, n-1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])

                        while l<r and nums[l] == nums[l+1]:
                            l += 1

                        while l<r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return ans




# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here