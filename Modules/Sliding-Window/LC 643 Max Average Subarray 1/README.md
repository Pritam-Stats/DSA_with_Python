# Maximum Average Subarray I – LeetCode 643

**Problem Link:**  
[LeetCode 643 – Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75)

## Problem Summary

Given an array of integers `nums` and an integer `k`, find the contiguous subarray of length `k` that has the maximum average value, and return this value. The answer should be a floating-point number.

---

## 📄 Brute_Force_TLE.py

### 🔍 Approach:
- Iterate over all possible subarrays of length `k`.
- For each subarray, calculate its sum and keep track of the maximum average.

### 🧠 Concepts Used:
- Sliding window logic (without actual optimization)
- Subarray traversal
- Basic list slicing

### ⏱ Time Complexity:
- **O(n * k)** — For each possible starting index, a new sum of `k` elements is computed.

### 📦 Space Complexity:
- **O(1)** — Only a few variables are used; no extra data structures.

### ❌ Limitation:
- This solution is inefficient for large inputs and will result in **TLE (Time Limit Exceeded)** on LeetCode.

---

## 📄 Sliding_Window_Optimal.py

### 🔍 Approach:
- Use the **sliding window** technique.
- Calculate the sum of the first `k` elements to initialize the window.
- Slide the window across the array by removing the element going out and adding the one coming in.
- Track the maximum sum throughout the process.

### 🧠 Concepts Used:
- Sliding window (optimized)
- Prefix sum logic (implicitly)
- Constant time window update

### ⏱ Time Complexity:
- **O(n)** — Each element is processed once while sliding the window.

### 📦 Space Complexity:
- **O(1)** — Only a few variables are used.

### ✅ Advantage:
- Efficient and optimal for large datasets.
- Passes all test cases on LeetCode.

---

## ✅ Recommendation

Always prefer the **Sliding Window** method for problems involving fixed-size subarrays where you need to compute max/min/sum/average, as it reduces time complexity significantly.
