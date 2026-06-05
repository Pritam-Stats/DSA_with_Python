from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ##classic problem.
        ## voting problem / Moore's Algorithm
        ## treat every elem as a potential candidate
        # reassign a candidate if vote becomes zero

        winner = None
        vote = 0
        for candidate in nums:
            if vote == 0:
                winner = candidate
            
            vote += (+1 if candidate == winner else -1)
            ## decrease the vote of the current leading candidate if a new candidate get's vote
            ## so at balance eventually the vote will become zero
        return winner
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here