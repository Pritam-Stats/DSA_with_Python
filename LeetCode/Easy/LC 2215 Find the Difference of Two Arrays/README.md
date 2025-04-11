# LeetCode 2215 - Find the Difference of Two Arrays

📌 [Problem Link - Find the Difference elements between two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75)

## 🧩 Problem Description

You're given two integer arrays `nums1` and `nums2`. The task is to return a list of two lists:

- The first list should contain all **distinct integers** that are in `nums1` but **not** in `nums2`.
- The second list should contain all **distinct integers** that are in `nums2` but **not** in `nums1`.

Duplicates in the original arrays should be ignored when computing the final result. Each result list must contain **only unique elements**, and the order of elements in the output does not matter.

---

## ✅ Approach & Solution

### Step 1: Remove Duplicates Using Sets

To focus only on **unique elements**, both arrays are converted into sets:

- `set1 = set(nums1)`
- `set2 = set(nums2)`

This automatically removes all duplicates and allows efficient set operations.

### Step 2: Perform Set Difference

To find elements that are only in one array and not in the other:

- `only_in_nums1 = set1 - set2`: Gives elements in `nums1` but not in `nums2`.
- `only_in_nums2 = set2 - set1`: Gives elements in `nums2` but not in `nums1`.

These are classic **set difference operations**, or in set theory:
```
A - B ≡ A ∩ Bᶜ
```

### Step 3: Convert to List and Return

The result is returned as a list of two lists:
```python
return [list(only_in_nums1), list(only_in_nums2)]
```

---

## 🕒 Time and Space Complexity

- **Time Complexity**: `O(n + m)`  
  Where `n` and `m` are the lengths of `nums1` and `nums2`, respectively.
  
- **Space Complexity**: `O(n + m)`  
  Due to the use of sets to store unique elements.

---

## 🔍 Summary

This solution is clean, efficient, and leverages the power of set operations to solve the problem with minimal code and optimal performance. It works equally well in Python, C++, or any language that supports basic set operations.


