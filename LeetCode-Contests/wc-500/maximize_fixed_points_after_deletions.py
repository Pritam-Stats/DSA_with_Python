##         --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline


# Link: https://leetcode.com/problems/maximize-fixed-points-after-deletions/description/
## LC: 3920

# ================================
# Author: Pritam
# ================================


class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        pass

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
        arg1 = inlt()
        # arg2 = ins()
        
        sol = Solution()
        res = sol.maxFixedPoints(arg1)
        
        print_lc(res)