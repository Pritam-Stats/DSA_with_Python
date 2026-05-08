from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    ##to optimize further we can write our own power func
    MOD = 10**9 + 7

    def power(self, x, n, mod):
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        
        res = self.power(x, n//2, mod)
        if n&1 == 0: #even
            res *= res
        else:
            res = res*res*x
        return res % mod


    def countGoodNumbers(self, n: int) -> int:
          
        ## how many numbers are possible such that even numbers are at even pos
        ## and prime numbers are at odd pos

        ## let n = 5
        ## _ _ _ _ _    #odd position has how many choices?? {2, 3, 5, 7} 4
        ##even pos has how many choices?? {0, 2, 4, 6, 8,}  ## 5
        ## how many even positions are there?? ## (n+1)//2
        ## how many odd positions are there?? ## (n)//2
        even_count = (n+1)//2
        odd_count = n//2
        ans = ((self.power(5, even_count, self.MOD)) * (self.power(4, odd_count, self.MOD)))%self.MOD    ##we have to optimize the pow
        return ans

    ## TC: O(log n)
    ## SC: O(1)
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here