#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    # swap
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse
        for arr in matrix:
            arr.reverse()
        return matrix
        
# @lc code=end

