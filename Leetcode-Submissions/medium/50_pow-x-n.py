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
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = abs(n)
        
        res = self.myPow(x, n//2)   ##half of the power
        if n&1 == 0:
            res = res*res
        else:
            res = res*res*x ##odd power
        return res
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here