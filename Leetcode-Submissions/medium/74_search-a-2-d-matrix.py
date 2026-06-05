from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # simple binary search in a matrix
        row = len(matrix)
        col = len(matrix[0])

        n = row*col
        low, high = 0, n-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            midCellValue = matrix[mid//col][mid % col]
            '''
            ## how row is calculated? -> think as a long 1d array, each col as fixed len, 
            # so if we divide by the col len, we can get how many rows are needed => curr row
            ## col is simple -> the reminder after dividing by the number of col will give 
            # the curr col
            '''
            if midCellValue == target:
                return True
            elif midCellValue > target:
                high -= 1
            else:
                low += 1
        return False

    # TC: O(log n*m)
    # SC: O(1)


# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
