# Maximum Sum Circular Subarray (Leetcode 918)

## Problem Statement
Given a **circular** array `arr`, return the maximum possible sum of a **non-empty** subarray.
- A **subarray** is a contiguous part of an array.
- Since the array is **circular**, subarrays can wrap around from the end of the array back to the beginning.

## Understanding the Problem with Examples

### Example 1
**Input:**
```
arr = [1, -2, 3, -2]
```
**Output:**
```
3
```
**Explanation:** The maximum subarray is `[3]`, which has a sum of `3`.

### Example 2
**Input:**
```
arr = [5, -3, 5]
```
**Output:**
```
10
```
**Explanation:** The maximum subarray is `[5, 5]` (circular wrap around), which has a sum of `10`.

### Example 3 (All Negative Case)
**Input:**
```
arr = [-3, -2, -3]
```
**Output:**
```
-2
```
**Explanation:** The maximum subarray is `[-2]`, which has a sum of `-2`.

---

## Approach & Thought Process

### 1. Two Possible Cases
- **Normal Maximum Subarray Sum** (Kadane’s Algorithm)  
  - This is the maximum subarray sum for a **linear** array.
- **Circular Maximum Subarray Sum**  
  - This is calculated as:  
    ```
    circularSum = Total Array Sum - Minimum Subarray Sum
    ```
  - **Why does this work?**
    - The **"circular"** maximum sum means we take **everything except the minimum subarray sum**.

### 2. Edge Case (All Negative Numbers)
- If all elements are **negative**, then `totalSum - minSum` becomes `0`, which is **wrong**.
- **Fix:** If `maxSum < 0`, return `maxSum` directly.

---

## Dry Run of the Approach

### Test Case
```
arr = [5, -3, 5]
```

#### Step 1: Initialize Variables
```
maxSum = -inf
minSum = +inf
totalSum = 0
currMaxSum = 0
currMinSum = 0
```

#### Step 2: Traverse the Array

| Index | arr[i] | currMaxSum | maxSum | currMinSum | minSum | totalSum |
|--------|--------|------------|--------|------------|--------|------------|
| 0 | 5 | 5 | 5 | 5 | 5 | 5 |
| 1 | -3 | 2 | 5 | -3 | -3 | 2 |
| 2 | 5 | 7 | 7 | 2 | -3 | 7 |

#### Step 3: Compute Circular Sum
```
circularSum = totalSum - minSum = 7 - (-3) = 10
```

#### Step 4: Check Edge Case (All Negative Numbers)
- `maxSum = 7`, which is **not negative**, so we take:
```
max(7, 10) = 10
```
Correct Output!

---

## Complexity Analysis

| Step | Operation | Time Complexity |
|------|-----------|----------------|
| Find max subarray sum (Kadane’s) | O(n) | O(n) |
| Find min subarray sum (Kadane’s) | O(n) | O(n) |
| Compute circular sum | O(1) | O(1) |
| Check edge case | O(1) | O(1) |
| **Total Complexity** | **O(n)** | **O(1)** |

- **Time Complexity:** `O(n)` since we iterate through the array once.
- **Space Complexity:** `O(1)` since we use only a few extra variables.

---

## Key Takeaways
- **Kadane’s Algorithm** is used to find both **maximum** and **minimum** subarray sums.  
- **Circular subarray sum** is computed using `totalSum - minSum`.  
- **All negative numbers** are handled separately (`if maxSum < 0`).  
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(1)`.  

---

