##         --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline


# Link: https://leetcode.com/problems/minimum-cost-to-move-between-indices/
## LC: 3919

# ================================
# Author: Pritam
# ================================


class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        ans = [0]*len(queries)
        cl = [0]*n
        for x in range(n):
            currClose = float("inf")
            for y in range(n):
                if x != y:
                    d = abs(nums[x] - nums[y])
                    if currClose > d:
                        currClose = d
                        cl[x] = y

        # return cl
        qi = 0
        for q in queries:
            l, r = q
            cost = 0
            if l > r:
                path = list(range(l, r-1, -1))
                for i in range(len(path) - 1):
                    x = path[i]
                    y = path[i+1]
                    if cl[x] == y:
                        cost += 1
                    else:
                        cost += abs(nums[x] - nums[y])
            else:
                path = list(range(l, r+1))
                for i in range(len(path) - 1):
                    x = path[i]
                    y = path[i+1]
                    if cl[x] == y:
                        cost += 1
                    else:
                        cost += abs(nums[x] - nums[y])

            ans[qi] = cost
            qi += 1

        return ans



## TC: O(n^2)
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
        q = inp()
        arg2 = []
        for _ in range(q):
            qn = inp()
            arg2.append(inlt())
        
        sol = Solution()
        res = sol.minCost(arg1, arg2)
        
        print_lc(res)