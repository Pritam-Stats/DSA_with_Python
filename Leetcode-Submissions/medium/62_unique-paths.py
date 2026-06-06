from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #math way
        return math.comb(m+n-2, m-1)
    
    ## TC: O(min(n, m))
    ## SC: O(1)

## Later TODO DP
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here