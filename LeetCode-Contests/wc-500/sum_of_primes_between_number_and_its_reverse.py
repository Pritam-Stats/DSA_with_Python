##         --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline


# Link: https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/
## LC: 3918

# ================================
# Author: Pritam
# ================================


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])

        mn, mx = min(n, r), max(n, r)

        isPrime = [True]*(mx+1)

        isPrime[0] = isPrime[1] = False
        i = 2
        while i*i <= mx:
            if isPrime[i]:
                for j in range(i*i, mx+1, i):
                    isPrime[j] = False
            i += 1

        ans = 0

        for x in range(mn, mx+1):
            if isPrime[x]:
                # ans.append(x)
                ans += x

        return ans

## TC: O(n* log log n)
## SC: O(n)


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
        res = sol.sumOfPrimesInRange(n)
        
        print_lc(res)