# Arrays

Arrays store elements in contiguous memory and allow constant-time indexing.

Most interview problems reduce to array manipulation, constraint handling, and pattern recognition.

This folder contains:

* Array-based problems
* Technique summaries
* Algorithm notes
* Revision references

Mastering arrays builds the foundation for advanced DSA.

---

# Core Techniques in Arrays

Below are the major techniques used in array problems, with detailed conceptual notes.

---

# 1️⃣ Basic Traversal & Simulation - Linear Search

## Linear Search
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
## When to Use

* Simple processing
* Counting
* Rearrangement
* Brute-force baseline

## Key Concepts

* Index control
* Boundary handling
* In-place updates
* Multiple passes

## Common Mistakes

* Off-by-one errors
* Incorrect loop ranges
* Modifying array while iterating incorrectly

## Problems:
- [Print All Possible SubArrays](/Structures/Arrays/05-PrintAllSubArrays.py) What's the total number of possible sub-arrays?
- [Reverse Array in Normal way - Without restriction](/Structures/Arrays/03-ReverseArray.py)
---
# Binary Search
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
### Time:
- At every operation the number of arr is getting 1/2
- so for n iteration, we will have (1/2)^n this is the formula of log(N)
- O(logN) - so for a array size of n, we need to have logN number of iteration at max
---

# Kadane's Algorithm
## Core use
Classical Problem : [LC 53 Max SubArray Sum](https://leetcode.com/problems/maximum-subarray/) | [Solution](/Structures/Arrays/06-MaxSubArraySum.py)

## Key Intuition:
- Keep track of maxsum and currsum. 
- If currsum becomes negative re-assign it to 0.

---

# 2️⃣ Two Pointers

## Core Idea

Use two indices moving through the array with a maintained invariant.

## Types

* Opposite ends (`l`, `r`)
* Same direction (slow-fast)
* Partition pointers

## When to Use
* [Reverse an Array Using Two Pointer O(1) Space](/Structures/Arrays/03-ReverseArray.py)
* Sorted arrays
* Pair sum problems
* Removing duplicates
* Reversals
* Partitioning

## Invariant Thinking

Always define:

* What does left represent?
* What does right represent?
* What condition keeps loop valid?

## Example Pattern

If sorted:

* sum < target → left++
* sum > target → right--

Time: Usually O(n)

---

# 3️⃣ Sliding Window

Derived from two pointers.

## Core Idea

Maintain a window that expands and contracts based on a constraint.

## Types

### Fixed Size

Window length = k

### Variable Size

Expand until invalid, then shrink.

## When to Use

* Subarray with condition
* Longest/shortest substring problems
* Maximum/minimum window problems

## Invariant

Window must always satisfy condition before updating result.

## Common Mistakes

* Forgetting to shrink properly
* Not updating answer at correct time

Time: O(n)

---

# 4️⃣ Prefix Sum

## Core Idea

Precompute cumulative sums to answer range queries efficiently.

```
prefix[i] = prefix[i-1] + arr[i]
```

## When to Use

* Range sum queries
* Subarray sum equals K
* Count subarrays

## Advanced Insight

If:
prefix[j] - prefix[i] = K
Then:
prefix[j] = prefix[i] + K

Use hashmap to store prefix frequencies.

Time: O(n)

---

# 5️⃣ Hashing with Arrays

## Core Idea

Trade space for time.

## When to Use

* Need O(1) lookup
* Detect duplicates
* Frequency counting
* Complement search (Two Sum unsorted)

## Pattern

Store what you have seen so far.

## Common Mistake

Forgetting edge case when element equals target itself.

---

# 6️⃣ Binary Search

## Core Idea

Exploit sorted order or monotonic condition.

## Variants

* Exact search
* Lower bound
* Upper bound
* Search in rotated array
* Binary search on answer

## Key Principle

Reduce search space by half each iteration.

## Template Thinking

Always define:

* What condition makes answer valid?
* What is the monotonic property?

Time: O(log n)

---

# 7️⃣ Sorting + Greedy

## Core Idea

Sort to simplify constraints, then make optimal local choices.

## When to Use

* Interval problems
* Height minimization
* Meeting room problems
* Pairing problems

## Key Thinking

After sorting:

* What greedy choice is safe?
* Why does it not break future choices?

Time: O(n log n)

---

# 8️⃣ Kadane’s Algorithm

## Problem Type

Maximum subarray sum.

## Core Idea

Maintain running sum.
If running sum becomes negative → reset.

```
current = max(arr[i], current + arr[i])
```

## Why It Works

Negative prefix reduces future sum.

Time: O(n)

Variants:

* Circular subarray
* Minimum subarray

---

# 9️⃣ Monotonic Stack

## Core Idea

Maintain stack in increasing or decreasing order.

## When to Use

* Next greater/smaller element
* Histogram area
* Stock span

## Why It Works

Each element is pushed and popped at most once.

Time: O(n)

---

# 🔟 Heap (Priority Queue)

## Core Idea

Maintain smallest/largest elements efficiently.

## When to Use

* Kth largest
* Top K frequent
* Sliding window maximum

Time: O(n log k)

---

# 1️⃣1️⃣ Bit Manipulation

## Used For

* Single number problems
* XOR-based tricks
* Mask filtering

## Key Properties

* a ^ a = 0
* a ^ 0 = a

Often reduces space complexity.

---

# 1️⃣2️⃣ Divide & Conquer

## Core Idea

Break array into halves and solve recursively.

## Algorithms

* Merge sort
* Quick sort
* Counting inversions
* Majority element (divide approach)

Time: Usually O(n log n)

---

# 1️⃣3️⃣ Dynamic Programming on Arrays

Many DP problems operate on sequences.

## Key Patterns

* 1D DP
* LIS
* Subset sum
* Partition problems

## Key Step

Define:

* State
* Transition
* Base case

---

# Common Array Mistakes

* Off-by-one errors
* Not handling empty input
* Overflow in prefix sums
* Incorrect binary search boundaries
* Forgetting to reset variables

---

# Mastery Order (Follow This Strictly)

1. Traversal
2. Two pointers
3. Sliding window
4. Prefix sum
5. Hashing
6. Binary search
7. Kadane
8. Sorting + Greedy
9. Monotonic stack
10. DP

---

# Goal

After mastering arrays, you should:

* Instantly recognize subarray constraints
* Identify monotonic properties
* Apply correct technique within minutes
* Solve medium problems confidently
* Avoid repeated mistakes

Arrays are the foundation of high-level problem solving.

---

