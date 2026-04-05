# LeetCode 53 - Maximum Subarray Sum
> Link: https://leetcode.com/problems/maximum-subarray/description/
## Problem Statement
Given an integer array `nums`, find the `subarray` with the **largest sum**, and return its **sum**.

### Constraints:
- The array can contain both positive and negative numbers.
- At least one element is present in the array.

### Example:
#### Input:
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```
#### Output:
```
6
```
#### Explanation:
The contiguous subarray `[4, -1, 2, 1]` has the maximum sum `6`.

---

## Approach - Kadane's Algorithm
To solve this problem efficiently, we use **Kadane’s Algorithm**, which is based on **dynamic programming**.

### Steps:
1. **Initialize variables**:
   - `maxSum = -∞` (to store the maximum subarray sum found so far).
   - `currSum = 0` (to track the sum of the current subarray).

2. **Iterate through the array**:
   - Add the current element to `currSum`.
   - Update `maxSum` with the maximum of `maxSum` and `currSum`.
   - If `currSum` becomes negative, reset it to `0` (starting a new subarray is more beneficial than keeping a negative sum).

3. **Return `maxSum`** as the final answer.

---

## Dry Run with Examples

### Example 1:
#### Input:
```
nums = [-2, -3, 4, -1, -2, 1, 5, -3]
```
#### Iteration:
| i  | arr[i] | currSum (Before) | currSum (After) | maxSum  |
|----|--------|-----------------|-----------------|---------|
| 0  | -2     | 0               | -2              | -2      |
| 1  | -3     | 0               | -3              | -2      |
| 2  | 4      | 0               | 4               | 4       |
| 3  | -1     | 4               | 3               | 4       |
| 4  | -2     | 3               | 1               | 4       |
| 5  | 1      | 1               | 2               | 4       |
| 6  | 5      | 2               | 7               | 7       |
| 7  | -3     | 7               | 4               | 7       |
#### Output:
```
7
```

---

### Example 2:
#### Input:
```
nums = [-2, -4, -6, -1, -3]
```
#### Iteration:
| i  | arr[i] | currSum (Before) | currSum (After) | maxSum  |
|----|--------|-----------------|-----------------|---------|
| 0  | -2     | 0               | -2              | -2      |
| 1  | -4     | 0               | -4              | -2      |
| 2  | -6     | 0               | -6              | -2      |
| 3  | -1     | 0               | -1              | -1      |
| 4  | -3     | 0               | -3              | -1      |
#### Output:
```
-1
```

---

## C++ Implementation
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxSubArraySum(vector<int>& arr) {
    int maxSum = INT_MIN; // Initialize maxSum to smallest possible value
    int currSum = 0; // Current subarray sum
    
    for (int i = 0; i < arr.size(); i++) {
        currSum += arr[i]; // Add current element to subarray sum
        maxSum = max(maxSum, currSum); // Update maxSum if needed
        
        if (currSum < 0) // If sum goes negative, reset it to 0
            currSum = 0;
    }
    
    return maxSum; // Return the maximum sum found
    }
};

```

---

## Complexity Analysis
- **Time Complexity**: **O(n)** (since we traverse the array only once).
- **Space Complexity**: **O(1)** (only a few extra variables are used, no additional data structures).

---

## Summary
- **Kadane’s Algorithm** efficiently finds the maximum sum of a contiguous subarray in **O(n)** time.
- If `currSum` goes negative, we reset it to `0` since starting fresh is better.
- This approach works for **both positive and negative numbers** and handles all negative values correctly.
- The **C++ implementation** follows the same logic as the Python code, ensuring efficiency.

Happy Coding! 🚀

