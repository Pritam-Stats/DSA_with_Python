##         --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline

'''
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


# Link: https://leetcode.com/problems/generate-parentheses/submissions/1999962733/
## LC: 22

# ================================
# Author: Pritam
# ================================

## ACCEPTED
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## given n pairs
        ans = []
        def f(curr:str, openLeft:int, closeLeft:int):
            if openLeft == 0 and closeLeft == 0:
                ans.append(curr)
                return
            
            if openLeft > 0:
                f(curr + "(", openLeft-1, closeLeft)

            
            if closeLeft > openLeft:
                f(curr+")", openLeft, closeLeft-1)

        f("", n, n)
        return ans

## TC: 
## SC: 


# ---------- LC Input Helpers ----------
def ceil(a, b):    ##relation b/w floor division and ceil division
    return (a+b-1)//b
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()

def print_lc(res):
    if isinstance(res, bool):
        print("true" if res else "false")
    elif isinstance(res, str):
        print(res)
    else:
        print(str(res).replace(' ', ''))


# ---------- Local Runner ----------
if __name__ == "__main__":
    # t = 1
    t = int(input().strip())

    for _ in range(t):
        n = inp()
        # arg1 = inlt()
        # arg2 = ins()
        
        sol = Solution()
        res = sol.generateParenthesis(n)
        
        print_lc(res)