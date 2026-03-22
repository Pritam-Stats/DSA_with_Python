- [1. Arrays](#1-arrays)
- [2. Core Techniques in Arrays](#2-core-techniques-in-arrays)
- [3. 1️⃣ Basic Traversal \& Simulation - Linear Search](#3-1️⃣-basic-traversal--simulation---linear-search)
  - [3.1. Linear Search](#31-linear-search)
  - [3.2. When to Use](#32-when-to-use)
  - [3.3. Key Concepts](#33-key-concepts)
  - [3.4. Common Mistakes](#34-common-mistakes)
  - [3.5. Problems:](#35-problems)
- [4. Binary Search](#4-binary-search)
    - [4.0.1. Time:](#401-time)
- [5. Kadane's Algorithm](#5-kadanes-algorithm)
  - [5.1. Core use](#51-core-use)
  - [5.2. Key Intuition:](#52-key-intuition)
- [6. Trapping Rainwater:](#6-trapping-rainwater)
      - [6.0.0.1. Some detail notes](#6001-some-detail-notes)
    - [6.0.1. Sorting Algorithms](#601-sorting-algorithms)

# 1. Arrays

Arrays store elements in contiguous memory and allow constant-time indexing.

Most interview problems reduce to array manipulation, constraint handling, and pattern recognition.

This folder contains:

* Array-based problems
* Technique summaries
* Algorithm notes
* Revision references

Mastering arrays builds the foundation for advanced DSA.

---

# 2. Core Techniques in Arrays

Below are the major techniques used in array problems, with detailed conceptual notes.

---

# 3. 1️⃣ Basic Traversal & Simulation - Linear Search

## 3.1. Linear Search
- Simple Algo to search for a target
- Can be applied to any array sorted or unsorted
- Travel the array one by one and returns for the first target.
- If target is 10 there are two 10’s linear search will return the index for the first 10
    ```Python
        arr = [2,4, 6, 8, 10, 12, 10, 14, 16]

        def linearSearch(arr: list, target: int):
            n = len(arr)
            for i in range(n):
                if arr[i] == target:
                    return i
            return -1   #if not found

        print(linearSearch(arr, 10))    #4
        print(linearSearch(arr, 0))     #-1
    ```
## 3.2. When to Use

* Simple processing
* Counting
* Rearrangement
* Brute-force baseline

## 3.3. Key Concepts

* Index control
* Boundary handling
* In-place updates
* Multiple passes

## 3.4. Common Mistakes

* Off-by-one errors
* Incorrect loop ranges
* Modifying array while iterating incorrectly

## 3.5. Problems:
- [Print All Possible SubArrays](/Structures/Arrays/05-PrintAllSubArrays.py) What's the total number of possible sub-arrays?
- [Reverse Array in Normal way - Without restriction](/Structures/Arrays/03-ReverseArray.py)
---
# 4. Binary Search
- **For Sorted Array**
- Take two idx st = 0 end = n-1
- Find the mid (int)
- Now compare the mid with the target
    - If equal then return
    - if mid value is > target
        - means our target will be in the left side of the mid (since the arr is sorted)
        - agar mid value hi target se bada h, toh aage ka sab value toh bada hi hogaa.
        - Update: end = mid -1
    - ***So now our search space became half in one iteration***
    - if mid is < target, then search in the right side. so
        - Update: st = mid+1
- So this will give a better time complexity
- So we have to repeat this till we get to a single element so till **`st ≤ end`**
- Here the equal to is important because we can have a single element left at the end.
- return -1 at the outside of the loop

- [BINARY SEARCH CODE](/Structures/Arrays/04-BinarySearch.py)
### 4.0.1. Time:
- At every operation the number of arr is getting 1/2
- so for n iteration, we will have (1/2)^n this is the formula of log(N)
- O(logN) - so for a array size of n, we need to have logN number of iteration at max
---

# 5. Kadane's Algorithm
## 5.1. Core use
Classical Problem : [LC 53 Max SubArray Sum](https://leetcode.com/problems/maximum-subarray/) | [Solution](/Structures/Arrays/06-MaxSubArraySum.py)

## 5.2. Key Intuition:
- Keep track of maxsum and currsum. 
- If currsum becomes negative re-assign it to 0.

---

# 6. [Trapping Rainwater](/08-trapping-rainwater.py): 
- have two arrays.
  1. To store the left largest for each bar (will st from id 1)
  2. To store the right largest for each bar (need to st from the right (id n-2) of the arr till id 0)
- now for each bar what can be the stored water
- stored water can't be negative

#### 6.0.0.1. Some detail notes
- Problem Understanding
> Water traps at each position i based on the minimum of the tallest bar to its left and right, minus `height[i]`. If no such boundaries exist, no water traps there. This needs precomputing max heights from both directions.

**Approach 1: Precompute Max Heights**
Create two arrays: `left_max[i]` (max height from 0 to i) and `right_max[i]` (max height from i to end). Sum `min(left_max[i], right_max[i]) - height[i]` for all i
> Time: O(n), Space: O(n).
​

**Approach 2: Two Pointers (Optimal)**
Use left and right pointers starting at ends, track `max_left` and `max_right`. Move the pointer with smaller height, adding trapped water based on its max.
> Time: O(n), Space: O(1).

- Key intuition: Water at index `i` is limited by the **shorter** of the tallest bars on its left and right.

- Optimal method: Two-pointer technique with O(n) time and O(1) extra space. [youtube](https://www.youtube.com/watch?v=SHNMoumKE44)

- Initialize:
  - `left = 0`, `right = n - 1`  
  - `left_max = height[left]`, `right_max = height[right]`  
  - `water = 0`. [purpletutor](https://purpletutor.com/trapping-rain-water/)

- Invariant: At every step, the side with the smaller current height (or smaller max) determines the possible water level at that side. [neetcode](https://neetcode.io/solutions/trapping-rain-water)

- Loop while `left < right`:
  - If `height[left] <= height[right]`:
    - If `height[left] >= left_max`: update `left_max = height[left]`.  
    - Else: add `left_max - height[left]` to `water` (water trapped at `left`).  
    - Move `left += 1`. [github](https://github.com/mdmzfzl/NeetCode-Solutions/blob/main/02_Two_Pointers/05_Trapping_Rain_Water/0042-trapping-rain-water.py)
  - Else:
    - If `height[right] >= right_max`: update `right_max = height[right]`.  
    - Else: add `right_max - height[right]` to `water` (water trapped at `right`).  
    - Move `right -= 1`. [purpletutor](https://purpletutor.com/trapping-rain-water/)

- Reason this is correct:  
  - When `height[left] <= height[right]`, there is guaranteed to be some bar on the right at least as tall as `height[left]`, so the limiting factor for water at `left` is `left_max` only; right side cannot reduce it. [algo](https://algo.monster/liteproblems/42)
  - Symmetric logic holds when `height[right] < height[left]`. [enjoyalgorithms](https://www.enjoyalgorithms.com/blog/trapping-rain-water/)

- Stopping condition: When `left >= right`, all positions have been processed, and `water` holds the total trapped water. [github](https://github.com/mdmzfzl/NeetCode-Solutions/blob/main/02_Two_Pointers/05_Trapping_Rain_Water/0042-trapping-rain-water.py)

- Complexity:
  - Time: Single pass over array → O(n). [youtube](https://www.youtube.com/watch?v=SHNMoumKE44)
  - Space: Only a few scalar variables → O(1) extra space. [youtube](https://www.youtube.com/watch?v=SHNMoumKE44)



### 6.0.1. Sorting Algorithms
- [Go here](/basic-sorting-algos/)









