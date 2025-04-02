# Maximum Product Subarray

## Problem Statement
Given an integer array `arr`, find the contiguous subarray (containing at least one number) which has the largest product and return the product.

> **LeetCode 153** Link: https://leetcode.com/problems/maximum-product-subarray/description/

## Approach and Explanation

### Observations
1. If we multiply elements continuously and update the maximum product (`maxProd`), it can give us the answer.
2. However, the presence of zero and negative numbers affects the product:
   - A zero resets the product sequence.
   - Negative numbers can make the product smaller or larger depending on the count of negatives in a segment.
3. To handle this, we traverse the array twice:
   - **Left to Right (l_r)**: Multiplies elements from start to end.
   - **Right to Left (r_l)**: Multiplies elements from end to start.

### Algorithm
1. Initialize `maxProd` as negative infinity to track the maximum product.
2. Traverse the array from **left to right**:
   - If the product becomes zero, reset it to `1`.
   - Multiply `l_r` with the current element.
3. Simultaneously, traverse the array from **right to left**:
   - If the product becomes zero, reset it to `1`.
   - Multiply `r_l` with the current element.
4. Update `maxProd` with `max(maxProd, l_r, r_l)` at each step.
5. Return `maxProd`.

## Dry Run with Two Important Examples

### Example 1
#### Input:
```python
arr = [-1, -3, -10, 0, 60]
```
#### Stepwise Execution:

| Index | Element | Left to Right (`l_r`) | Right to Left (`r_l`) | `maxProd` |
|--------|---------|----------------|----------------|---------|
| 0      | -1      | -1             | 60             | 60      |
| 1      | -3      | 3              | 0              | 60      |
| 2      | -10     | -30            | 10             | 60      |
| 3      | 0       | Reset (1)       | 30             | 60      |
| 4      | 60      | 60              | -1             | 60      |

#### Output:
```python
60
```

---

### Example 2
#### Input:
```python
arr = [2, 3, -2, 4, -1]
```
#### Stepwise Execution:

| Index | Element | Left to Right (`l_r`) | Right to Left (`r_l`) | `maxProd` |
|--------|---------|----------------|----------------|---------|
| 0      | 2       | 2              | -1             | 2       |
| 1      | 3       | 6              | -4             | 6       |
| 2      | -2      | -12            | 8              | 8       |
| 3      | 4       | -48            | -16            | 8       |
| 4      | -1      | 48             | -32            | 48      |

#### Output:
```python
48
```

## Time and Space Complexity Analysis

- **Time Complexity:** `O(N)`
  - We traverse the array twice (once left to right and once right to left).
- **Space Complexity:** `O(1)`
  - We use only a few extra variables (`maxProd`, `l_r`, `r_l`), which is constant space.

## Brute Force Approach (Python)

A naive approach checks the product of all subarrays and keeps track of the maximum product.

```python
def maxProductBruteForce(arr):
    n = len(arr)
    maxProd = float('-inf')
    
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            maxProd = max(maxProd, product)
    
    return maxProd

# Example
print(maxProductBruteForce([-2, 6, -3, -10, 0, 2]))  # Output: 180
```

### Complexity of Brute Force Approach:
- **Time Complexity:** `O(N^2)`, since we check every subarray.
- **Space Complexity:** `O(1)`, as only a few variables are used.

## Optimized Approach (C++ Version)
 - The one we did in Python

```cpp
#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

int maxProduct(vector<int>& arr) {
    int n = arr.size();
    int maxProd = INT_MIN;
    
    int l_r = 1;
    int r_l = 1;
    
    for (int i = 0; i < n; i++) {
        if (l_r == 0) l_r = 1;
        if (r_l == 0) r_l = 1;
        
        l_r *= arr[i];
        r_l *= arr[n - i - 1];
        
        maxProd = max({maxProd, l_r, r_l});
    }
    
    return maxProd;
}

int main() {
    vector<int> arr = {-2, 6, -3, -10, 0, 2};
    cout << maxProduct(arr) << endl; // Output: 180
    return 0;
}
```

## Conclusion
- We optimized the problem using two traversals (left to right and right to left) instead of checking all subarrays.
- This reduced the time complexity from `O(N^2)` (brute force) to `O(N)`.
- The approach efficiently handles negative numbers and zeros to compute the maximum product subarray.

