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

    i = 0
    while i < n:
        currElm = nums[i]
        correctIdx = nums[i] #correct idx of the element

        if (nums[correctIdx] != nums[i]):
            #swap place at the correct idx
            nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
        else:
            i += 1
    print(nums) #cyclic sort

    print("Repeat = ", end="  ")
    for i in range(n):
        if i != nums[i]:
            print(nums[i], end= " ")

    print("\nMissing = ", end="  ")
    for i in range(n):
        if i != nums[i]:
            print(i, end=" ")



# ---------- Main ----------
if __name__ == "__main__":
    t = 1
    # t = inp()
    for _ in range(t):
        solve()