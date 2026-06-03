from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        ##reverse rows
        for row in matrix:
            row.reverse()
        
        return matrix
        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here