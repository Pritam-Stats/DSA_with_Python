from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## better approach - voting
        c1, c2 = None, None
        v1, v2 = 0, 0
        for x in nums:
            if c1 == x: ##check first -> one mistake here
                v1 += 1
            elif c2 == x:
                v2 += 1
            elif v1 == 0:   #this can't be the first check
                c1 = x
                v1 = 1
            elif v2 == 0:
                c2 = x
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1
        
        ## but we might not have two answers - verify the count as well

        cnt1, cnt2 = 0, 0
        #we have two candidates
        n = len(nums)
        for x in nums:
            cnt1 += (c1 == x)   #true = 1
            cnt2 += (c2 == x)

        return [c for c, cnt in [(c1, cnt1), (c2, cnt2)] if c != None and cnt > n//3]

    ## TC: O(n)
    ## SC: O(1)


      


        '''
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        n = len(nums)
        ans = []
        for x in freq:
            if freq[x] > n//3:
                ans.append(x)
        return ans
    
    ## TC: O(n)
    ## SC: O(n)
        '''
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here