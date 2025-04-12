
# Leetcode 1207 – Unique Number of Occurrences 🧠  
🔗 [Problem Link - LC 1207](https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75)

---

## 📝 Problem

Given an array of integers, return `True` if the number of occurrences of each value is **unique**, otherwise return `False`.

---

## 💡 Approach

We use a **dictionary** to count how many times each number appears. Then we check if all the frequencies are **unique** using a **set**.

### DSA Concepts:
- Hashmaps (for counting occurrences)
- Sets (to check uniqueness)

---

## ✅ Why This Works

- We count how often each element appears using a hashmap.
- Then we check if all those frequency counts are unique by comparing the length of the list vs. set.
- If they match → all counts are unique.

---

## ⏱️ Time & Space Complexity

| Type        | Complexity |
|-------------|------------|
| Time        | O(n)       |
| Space       | O(n)       |

- `n` = number of elements in the array

---

## ✔️ Code (Python)

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for num in arr:
            occ[num] = occ.get(num, 0) + 1

        counts = list(occ.values())
        return len(counts) == len(set(counts))
```

---
