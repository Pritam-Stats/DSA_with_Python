

**Problem Link**: [LC 75 - Sort Colors](https://leetcode.com/problems/sort-colors/description/)
**Date**: June 18, 2025
**Topic**: \[\[2.1 Arrays]]
**Difficulty**: Medium

---

### Summary Description

Given an array containing only the integers `0`, `1`, and `2`, the task is to sort the array **in-place** without using any built-in sorting functions. The sorted order should have all 0s first, followed by 1s, and then 2s.

---

## Strategy & Key Insights

- Use three pointers: `low`, `mid`, and `high`.
- Also known as **DNF** (Dutch National Flag) Problem.
- The `mid` pointer is the main traversal pointer. Imagine the array divided into three regions:

  - Left (from start to `low-1`): contains 0s
  - Middle (from `low` to `mid-1`): contains 1s
  - Right (from `high+1` to end): contains 2s

- As we iterate:

  - If `nums[mid] == 0`: swap with `nums[low]`, then increment both `low` and `mid`.
  - If `nums[mid] == 1`: it's already in the correct region, just increment `mid`.
  - If `nums[mid] == 2`: swap with `nums[high]` and decrement `high`. Do **not** increment `mid` in this case, as the swapped element from `high` must be evaluated.

---

## Code (Optimal Logic)

```text
low, mid, high = 0, 0, n - 1
while mid <= high:
    if nums[mid] == 0:
        swap(nums[low], nums[mid])
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        swap(nums[mid], nums[high])
        high -= 1
```

---

## Time and Space Complexity

- **Time Complexity**: O(N) — Each element is visited at most once.
- **Space Complexity**: O(1) — In-place sorting using constant extra space.

