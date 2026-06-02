from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        n = len(prices)
        minP = float('inf')
        for p in prices:
            if p < minP:
                minP = p
            else:
                maxP = max(maxP, p - minP)
        return maxP




        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here