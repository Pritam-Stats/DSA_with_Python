# LeetCode 605: Can Place Flowers

🔗 [Problem Link](https://leetcode.com/problems/can-place-flowers/submissions/1596843160/?envType=study-plan-v2&envId=leetcode-75)

## Problem Statement

You are given an array `flowerbed`, where `0` means an empty plot and `1` means a plot already planted with a flower. You are also given an integer `n`, the number of new flowers to plant. Flowers cannot be planted in adjacent plots.

Return `True` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule, otherwise return `False`.

---

## 💡 Approach

We loop through the `flowerbed` and check if each position is a valid spot to plant a flower. A position is valid if:

- It is currently `0` (empty)
- The **left neighbor** is `0` or it’s the first plot
- The **right neighbor** is `0` or it’s the last plot

If the spot is valid:
- We "plant" a flower by marking it as `1`
- Increment a counter

If at any point the count of planted flowers reaches `n`, we can return early with `True`.

---

## 🧪 Dry Run Example

Input: flowerbed = [1, 0, 0, 0, 1] n = 1


- At index `2`, both neighbors are `0`, so we can plant a flower there.
- Count becomes `1`, which is enough.
- ✅ Return `True`

---

## ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n)`  
  Single pass through the array

- **Space Complexity:** `O(1)`  
  In-place updates, no extra space used

---

## ✅ Highlights

- Efficient **early exit** to save time once we've planted enough
- Clean logic using boundary checks for left/right neighbors
- Beats 96% in memory on LeetCode 💪

---


