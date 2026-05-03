import sys
from typing import *
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import math

# q1
# Link: https://leetcode.com/problems/count-indices-with-opposite-parity/description/
## LC: 3917


# ================================
# Author: Pritam
# ================================

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0]*n
        c = [1 if x % 2 == 0 else 0 for x in nums]
        # return c
        for i in range(n):
            cnt = 0
            for j in range(i+1, n):
                if c[i] == 0:
                    if c[j] == 1:
                        cnt += 1
                    ans[i] = cnt
                else:
                    if c[j] == 0:
                        cnt += 1
                    ans[i] = cnt

        return ans


# TC:
# SC:

# ---------- Local Runner ----------


# ---------- LC Input Helpers ----------
input = sys.stdin.readline

def ceil(a, b):  # relation b/w floor division and ceil division
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
        # This removes the default Python spaces from lists
        print(str(res).replace(' ', ''))



if __name__ == "__main__":
    # t = 1
    t = int(input().strip())

    for _ in range(t):
        n = inp()
        arg1 = inlt()
        # arg2 = ins()
        
        sol = Solution()
        res = sol.countOppositeParity(arg1)
        
        print_lc(res)