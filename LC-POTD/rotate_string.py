# Link https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-03
## LC 796



import sys
import json
from typing import *

import math
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter

# ================================
# Author: Pritam
# ================================

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s2 = s+s

        if goal not in s2:
            return False
        return True


## TC: O(n)
## SC: O(2n)

# ---------- Local Runner (CPH) ----------
if __name__ == "__main__":
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]

    if not lines:
        sys.exit(0)
    
    sol = Solution()
    args_count = 2  # Set this to the number of parameters your function takes
    
    if len(lines) % args_count == 1:
        lines.pop(0)
    
    for i in range(0, len(lines), args_count):
        args = []
        for j in range(args_count):
            line = lines[i+j]
            try:
                args.append(json.loads(line))
            except json.JSONDecodeError:
                args.append(line)
            
        res = sol.rotateString(*args)
        
        if isinstance(res, bool):
            print("true" if res else "false")
        elif isinstance(res, str):
            print(res)
        else:
            print(json.dumps(res).replace(' ', ''))