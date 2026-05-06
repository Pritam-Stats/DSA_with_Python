from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows):
            empty_slot = cols - 1
            for c in range(cols-1, -1, -1):
                if boxGrid[r][c] == "*":
                    empty_slot = c-1
                
                elif boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][empty_slot] = '.', "#"
                    empty_slot -= 1

        return [list(row) for row in zip(*boxGrid[::-1])]

    ## TC: O(m*n)
    ## SC: O(m*n)
# @lc code=end



if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here