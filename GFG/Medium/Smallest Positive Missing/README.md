# Smallest Positive Missing Number

## 🚀 Problem Statement

Given an array of integers, find the **smallest positive number** that is **missing from the array**.

For example:
- Input: `[2, -3, 4, 1, 1, 7]`
- Output: `3`

---

## 🎯 Goal

Find the **first smallest positive number** that is not present in the array.

We are **not** interested in:
- Negative numbers (`< 1`)
- Zeros (`0`)
- Numbers larger than the array size (we’ll see why below)

---

## 🔍 Key Observations

- For an array of size `n`, the **smallest missing number** must be in the range `1` to `n+1`.
- Example:
  - If all numbers from `1` to `n` are present → missing number = `n + 1`
  - If any number in between is missing → that is our answer.

This means we only care about numbers in the range `[1, n]`.

---

## 💡 Optimized Approach: Index Mapping

### Concept:

We **rearrange** the array such that:
- Every value `x` (where `1 <= x <= n`) is placed at index `x - 1`.

For example:
- `1` should be at index `0`
- `2` should be at index `1`
- ...
- `n` should be at index `n - 1`

We do this by **swapping elements** to their correct positions.

---

## 🔁 Dry Run Example

Input: `[2, -3, 4, 1, 1, 7]`  
Array size `n = 6`

### Step 1: Rearranging elements

We want:
- `1` at index `0`
- `2` at index `1`
- `3` at index `2`
- ...

We start scanning and **swap** if needed:
- Initial: [2, -3, 4, 1, 1, 7] 
- Swap 2 <-> 1: [4, -3, 2, 1, 1, 7] 
- Swap 4 <-> 1: [1, -3, 2, 4, 1, 7] Now 1 is in place. 
- Move ahead. Next: [1, -3, 2, 4, 1, 7] 
- Swap 2 <-> -3: [1, 2, -3, 4, 1, 7] Done.


Final arrangement: `[1, 2, -3, 4, 1, 7]`

### Step 2: Finding the missing number

Now scan the array:

- Index `0` → value = 1 → correct
- Index `1` → value = 2 → correct
- Index `2` → value = -3 → should be 3 → **missing number is 3**

✅ **Answer: 3**

---

## ⏱ Time & Space Complexity

### ✅ Time Complexity: `O(n)`
- Each element is moved/swapped at most **once**, so total work is linear.

### ✅ Space Complexity: `O(1)`
- Sorting and rearrangement are done **in-place**.
- No extra space used.

---

## 🙌 Summary

- We only care about numbers in `[1, n]`
- Negative numbers, 0, and values > `n` are **ignored**
- Place each valid number at its correct index using **swapping**
- Scan to find the first index `i` where `arr[i] != i + 1` → return `i + 1`

---

## 📘 Use Cases

- Interview problem
- Real-world: tracking missing IDs, order numbers, etc.
- Helps understand **in-place algorithms** and **index manipulation**

