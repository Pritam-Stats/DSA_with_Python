from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start

# ================================
# Author: Pritam
# ================================

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) #row
        m = len(matrix[0]) #col

        zeros = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.append(tuple([i, j]))

        if zeros:
            for row, col in zeros:
                matrix[row] = [0]*m
                for i in range(n):
                    matrix[i][col] = 0
        return matrix

                

        
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here