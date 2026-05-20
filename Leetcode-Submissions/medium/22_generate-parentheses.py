from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(open: int, close: int, n: int, path: list, ans: list):
            if open == n and close == n:
                ans.append(''.join(path[:]))
                return
            if open < n:
                path.append('(')
                f(open+1, close, n, path, ans)
                path.pop()

            if open > close:
                path.append(')')
                f(open, close+1, n, path, ans)
                path.pop()
        ans = []
        f(0, 0, n=n, path=[], ans=ans)
        return ans


# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
