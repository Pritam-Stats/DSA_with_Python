# Cyclic Sort | [Code](./cyclic_sort-return-repeating-and-missing-nums.py)

## Core Idea
Cyclic sort is used when:
- Array contains numbers in a **fixed range**
  - Either `1 … n` or `0 … n-1`
- Goal: place each element at its **correct index**

---

## Index Mapping

| Value Range | Correct Index |
|------------|--------------|
| `1 … n` | `x - 1` |
| `0 … n-1` | `x` |

---

## Invariant
At index `i`:
- If element is not at correct position → swap it to correct index
- Do **not move forward** until current index is correct

---

## Template

### For `1 … n`
```python3[]
i = 0
while i < n:
    correct = nums[i] - 1
    if nums[i] != nums[correct]:
        nums[i], nums[correct] = nums[correct], nums[i]
    else:
        i += 1

---

For 0 … n-1

i = 0
while i < n:
    correct = nums[i]
    if nums[i] != nums[correct]:
        nums[i], nums[correct] = nums[correct], nums[i]
    else:
        i += 1
```

---

### Key Condition (Very Important)

if nums[i] != nums[correct]:

Why:
- Prevents infinite loops
- Handles duplicates safely


---


Time & Space
- Time: O(n)
- Space: O(1)

Reason:
- Each element is swapped at most once into correct positionhttps://leetcode.com/problems/find-missing-and-repeated-values/

---

# Problem: Set Mismatch (LeetCode 645) | [Solution](./lc-645-set-Mismatch.py)

Problem Summary
- Array of size n
- Contains numbers 1 … n
- One number is duplicated
- One number is missing

---

Approach (Cyclic Sort)

Step 1: Place elements correctly

Use cyclic sort to try placing each number at index x - 1.

---

Step 2: Find mismatch

After sorting:
- If nums[i] != i + 1
- nums[i] → duplicate
- i + 1 → missing

---

Example
Input:

[1,2,2,4]

After cyclic sort:

[1,2,2,4]

Check:
- index 2 → expected 3, found 2

Output:

[2,3]

---

Key Takeaways
- Cyclic sort works when values map directly to indices
- Always maintain the invariant:
- “Keep swapping until correct element is placed”
- Duplicate case is handled by:
- nums[i] == nums[correct] → move forward


---

# Problem : [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values/) | [Solution](./lc-2965-find-missing-and-repeat-2d.py)


# Problem:[LC-448-Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

