##         --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline


# Link: https://leetcode.com/problems/single-number-ii/description/
## LC: 137

# ================================
# Author: Pritam
# ================================


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans =0
        for j in range(32):
            colSum = 0
            for x in nums:
                if (x>>j) & 1 == 1: ##set bit check
                    colSum +=1
            ##now check if the column is divisible by 3

            if colSum % 3 != 0:
                if j == 31:
                    ##sign bit
                    ans -= (1<<31)
                else:
                    ans |= (1<<j)

        return ans
            
## TC: O(31 * n)
## SC: O(1)


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
        res = sol.singleNumber(arg1)
        
        print_lc(res)