# Arrays

Arrays store elements in contiguous memory and allow O(1) indexing

Most problems reduce to:
- Traversal
- Constraint handling
- Pattern recognition

This section includes:
- Array problems
- Core techniques
- Algorithm patterns
- Revision notes

---

# Core Techniques in Arrays

---

## 1. Traversal & Simulation (Linear Search)

### Concept
- Iterate through array sequentially
- Works for both sorted and unsorted arrays
- Returns first occurrence of target

### When to Use
- Brute force baseline
- Counting / frequency
- Rearrangement
- Simulation problems

### Key Points
- Maintain correct index handling
- Be careful with boundaries
- In-place updates possible
- May require multiple passes

### Common Mistakes
- Off-by-one errors
- Incorrect loop ranges
- Modifying array incorrectly during iteration

### Problems
- [Print All Possible SubArrays](./05-PrintAllSubArrays.py)
- [Reverse Array in Normal way - Without restriction](./03-ReverseArray.py)

---

## 2. Binary Search

### Requirement
- Array must be sorted

### Core Idea
- Reduce search space by half every iteration

### Key Points
- Use `st <= end` to handle single element
- Mid divides search space
- If mid > target → move left
- If mid < target → move right

### Complexity
- Time: O(log n)

### Reference
- [Binary Search Code](./04-BinarySearch.py)

---

## 3. Kadane’s Algorithm

### Problem
- Maximum subarray sum  
- [LC 53 Max SubArray Sum](https://leetcode.com/problems/maximum-subarray/)  
- [Solution](./06-MaxSubArraySum.py)

### Intuition
- Maintain current sum and maximum sum
- If current sum becomes negative → reset
- Negative prefix is never useful

---

## 4. Trapping Rain Water

### Problem
- [Trapping Rainwater](/08-trapping-rainwater.py)

### Core Idea
- Water at index `i` = min(left_max, right_max) - height[i]
- Water cannot be negative

---

### Approach 1: Prefix Arrays
- Precompute:
  - left_max[i] → max from left
  - right_max[i] → max from right
- Compute water at each index

- Time: O(n)
- Space: O(n)

---

### Approach 2: Two Pointers (Optimal)

### Intuition
- Water is limited by smaller boundary
- Process the smaller side first

### Key Logic
- Maintain:
  - left pointer
  - right pointer
  - left_max
  - right_max

- If left height <= right height:
  - Use left_max to compute water
  - Move left pointer
- Else:
  - Use right_max
  - Move right pointer

### Complexity
- Time: O(n)
- Space: O(1)

---

# Summary

- Traversal → base for all problems
- Binary Search → sorted arrays, logarithmic optimization
- Kadane → optimal subarray problems
- Two Pointers → space optimized linear solutions


# LC 31 [Next Permutation](https://leetcode.com/problems/next-permutation/description/)
- [Code](./lc-31-next-permutation.py)

## Core Idea
[Page Link](https://ipritam.notion.site/LC-31-Next-permutation-33d3934632d280898dc2ced07f8b2586)

- Find the **next lexicographically greater permutation**
- If not possible → return smallest (sorted ascending)

<p align="center">
  <img src="https://ipritam.notion.site/image/attachment%3Ac7a94b5d-0670-41a4-9b18-28a87912817a%3Anse-6558044683171050071-1.jpeg.jpeg?table=block&id=33d39346-32d2-81e9-9e6a-e815bc634998&spaceId=9ae90934-1af9-4c64-80a1-7236bb37c003&width=2000&userId=&cache=v2" alt="Project Demo" width="600"/>
</p>
<p align="center">
  <img src="https://ipritam.notion.site/image/attachment%3Ae219089d-77cc-4c37-b564-413838b16d80%3Anse-628237487324672537-2.jpeg.jpeg?table=block&id=33d39346-32d2-81e7-b38f-efd848383168&spaceId=9ae90934-1af9-4c64-80a1-7236bb37c003&width=2000&userId=&cache=v2" alt="Project Demo" width="600"/>
</p>

---

## Steps

- Traverse from right → find first index `i` such that:
  - `nums[i] < nums[i+1]`
  - This is the **dip point**

- If no such index:
  - Array is in descending order (largest permutation)
  - Reverse entire array → smallest permutation

- Else:
  - From right → find element just greater than `nums[i]`
  - Swap them

- Reverse the subarray from `i+1` to end

---

## Key Intuition

- Right side after dip is always **descending**
- To get next permutation:
  - Make smallest possible increase
  - Then minimize the suffix

---

## Complexity

- Time: O(n)
- Space: O(1)

---

## Common Mistakes

- Forgetting to reverse suffix (not sort)
- Picking wrong swap element (must be just greater)
- Not handling fully descending case

---

## Pattern

- Permutation + Greedy + Two pointers (reverse suffix)