from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n can be negative

        if x == 1 or n ==0:
            return 1
        if x == 0:
            return 0
        if n == 1:
            return x
        
        if n < 0:
            n = abs(n)
            x = 1/x
        
        ans = 1
        while n:
            if n%2 == 0:
                #even power
                x *= x
            else:
                ans *= x
                x *= x
            n = n>>1
        return ans

## TC: O(log2 n)
## SC: O(1)
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here