
# LeetCode 42 - Trapping Rain Water

**Problem Link:** [Leetcode 42 - Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)
**Date:** June 13, 2025
**Topic:** \[\[2.1 Arrays]]
**Difficulty:** Hard

---

## Problem Summary

We are given an array `height[]` representing elevation heights where each bar has a width of 1. Imagine the bars as vertical lines on a histogram. Our goal is to **compute how much water can be trapped** between these bars after raining.

---

## Key Observations

* **Water traps in valleys**: A bar can trap water only if **there are taller bars on both sides**.
* For the `i-th` bar, the **maximum height** of the bars to the **left** and **right** determines how much water it can trap.
* If `left_max[i]` and `right_max[i]` are the tallest bars to the left and right of index `i`, then:

  ```
  water_at_i = min(left_max[i], right_max[i]) - height[i]
  ```

  (Only add this if it's positive - water can't have negative volume.)

---

## Intuition

* We traverse the array to **precompute the maximum heights to the left and right** of every index.
* For each position, compute the amount of trapped water using the formula above.
* Sum this across all bars to get the total trapped water.

---

## Example

```python
Input:  height = [4, 2, 0, 6, 3, 2, 5]
Output: 11
```

### Explanation:

```
         |
         |        |
|        |        |
|        |  |     |
|  |     |  |  |  |
|  |     |  |  |  |
4  2  0  6  3  2  5
```

* Water trapped above indices 1, 2, 4, 5.
* Total = 2 (idx 1) + 4 (idx 2) + 2 (idx 4) + 3 (idx 5) = **11**

---

## Brute Force Approach

### Pseudocode:

```
left_max[0] = height[0]
for i in 1 to n-1:
    left_max[i] = max(left_max[i-1], height[i])

right_max[n-1] = height[n-1]
for i in n-2 to 0:
    right_max[i] = max(right_max[i+1], height[i])

total = 0
for i in 0 to n-1:
    water = min(left_max[i], right_max[i]) - height[i]
    if water > 0:
        total += water
return total
```

### Time Complexity: `O(n)`

### Space Complexity: `O(n)`

---

## Optimal Approach (Two Pointer)

We can optimize space to `O(1)` using two pointers.

### Idea:

* Use two pointers (`left`, `right`) starting from both ends.
* Keep track of `left_max` and `right_max` dynamically.
* Move the pointer pointing to the smaller height.


### **Pseudocode – Two Pointer Approach**

```
Initialize:
    left = 0
    right = length of height - 1
    left_max = 0
    right_max = 0
    total_water = 0

While left < right:
    If height[left] < height[right]:
        If height[left] >= left_max:
            Update left_max to height[left]
        Else:
            Add (left_max - height[left]) to total_water
        Move left pointer to the right (left += 1)
    
    Else:
        If height[right] >= right_max:
            Update right_max to height[right]
        Else:
            Add (right_max - height[right]) to total_water
        Move right pointer to the left (right -= 1)

Return total_water
```


### Time Complexity: `O(n)`

### Space Complexity: `O(1)`

---

## Summary

| Approach    | Time | Space | Notes                                |
| ----------- | ---- | ----- | ------------------------------------ |
| Brute Force | O(n) | O(n)  | Uses `left_max` and `right_max` arrays |
| Two Pointer | O(n) | O(1)  | Optimal space                        |

---

