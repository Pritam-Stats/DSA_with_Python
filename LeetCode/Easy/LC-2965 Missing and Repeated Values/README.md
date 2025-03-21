# LC-2965: Find the Missing and Repeated Values in a Grid
> https://leetcode.com/problems/find-missing-and-repeated-values/
### Problem Statement

You are given a **0-indexed 2D integer matrix** `grid` of size `n × n` with values in the range `[1, n^2]`. Each integer appears **exactly once**, except for **one number 'a' which appears twice**, and **one number 'b' which is missing**.

The task is to find the **repeating** and **missing** numbers `a` and `b` and return them as an array `[a, b]`.

#### **Example 1**
- **Input:**
```python
grid = [[1, 3],
        [2, 2]]
```
- **Output:**
```python
[2, 4]
```
> **Explanation:** `2` is repeated twice, `4` is missing.

#### **Example 2**
- **Input:**
```python
grid = [[9, 1, 7],
        [8, 9, 2],
        [3, 4, 6]]
```
- **Output:**
```python
[9, 5]
```
> **Explanation:** `9` is repeated twice. `5` is missing.

---
## **Solution Approach 1 - NOT OPTIMIZED**
### **Steps to Solve the Problem**
1. Convert the **2D grid** into a **1D list** for easier processing.
2. Using a **dictionary (`freq`)** to count occurrences of each number as a frequency table.
3. Iterating through numbers **from `1` to `n^2`**:
   - If a number appears **twice**, store it as `a` (the repeated number).
   - If a number appears **zero times**, store it as `b` (the missing number).
4. Return `[a, b]`.

---
## **Pseudo-Code**
```
1. Create an empty list `arr_1d`
2. Convert `grid` into a 1D list `arr_1d`
3. Create an empty dictionary `freq`
4. Count occurrences of each number in `arr_1d`
5. Initialize variables `a = 0` and `b = 0`
6. Iterate from `1` to `n^2`:
    a. If `freq.get(num, 0) == 2`, set `a = num` (repeated number)
    b. If `freq.get(num, 0) == 0`, set `b = num` (missing number)
7. Return `[a, b]`
```
- Main funda was the use of get method of dictionaries
---

## **Time Complexity Analysis**
- **Converting 2D to 1D List** → `O(n^2)`
- **Counting occurrences using a dictionary** → `O(n^2)`
- **Checking numbers from `1` to `n^2`** → `O(n^2)` (worst case)
- **Overall Complexity**: **`O(n^2)`**
- **Space Complexity**: **`O(n^2)`**
---
## **Key Takeaways**
- **Dictionary `.get()` method** is useful to retrieve values and provide a default. Avoids key error.
- This problem can be solved using **mathematical formulas** (sum difference method), but using a dictionary is more intuitive.
- Understanding frequency maps (hashmaps) is crucial for such problems.

---
## **Alternative Approach (Without Dictionary)**
- Use **sum and square sum formulas** to find the missing and repeated numbers mathematically.
- This approach can achieve **O(n^2) time complexity**, but requires extra computation.

Hope this helps you understand the problem! 🚀

