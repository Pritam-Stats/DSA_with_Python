# --- imports ---
import sys
import math
from typing import *
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
input = sys.stdin.readline


# Link:
# LC:

# ================================
# Author: Pritam
# ================================


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


# TC: O(n^2)
# SC: O(1)


# ---------- LC Input Helpers ----------
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
        print(str(res).replace(' ', ''))


# ---------- Local Runner ----------
if __name__ == "__main__":
    # t = 1
    t = int(input().strip())

    for _ in range(t):
        n = inp()
        arg1 = []
        for _ in range(n):
            q = inp()
            row = inlt()
            arg1.append(row)
        # arg2 = ins()

        sol = Solution()
        res = sol.rotate(arg1)

        print_lc(res)
