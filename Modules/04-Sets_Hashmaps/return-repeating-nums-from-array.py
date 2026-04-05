# ================================
# Author: Pritam
# ================================


import sys
input = sys.stdin.readline
# ---------- Helpers ----------
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def ins():
    return input().strip()
def inmap():
    return map(int, input().split())
# ---------- Solve Function ----------

def solve():
    n = inp()
    nums = inlt()

    seen = set()
    repeat = set()

    for x in nums:
        if x in seen:
            repeat.add(x)
        else:
            seen.add(x)
        
    print(*repeat)

## best approach - CYCLIC SORT (../cyclic_sort.py)

# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve()