from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        
        ans = [[1]]     #0th row

        for i in range(1, n):
            prev = ans[-1]

            row = [1]
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])

            row.append(1)

            ans.append(row)
        return ans


# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
