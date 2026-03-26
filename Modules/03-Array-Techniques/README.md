

# 🧠 Vowel Strings in Ranges — Prefix Sum Approach
**Question LC 2559**: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
## 🔍 Intuition

The problem asks us to count how many words in a given range start **and** end with a vowel.

A brute-force approach would check each query range individually, leading to **O(n × q)** time complexity — which is inefficient for large inputs.

To optimize:

* First, identify which words are **valid** (start and end with vowels).
* Then, use a **prefix sum array** to quickly compute counts for any range.

---

## 🚀 Approach

### Step 1: Identify Valid Words (Contribution Array)
Create an array `contri` where:
* `contri[i] = 1` if `words[i]` starts **and** ends with a vowel
* Otherwise, `contri[i] = 0`

This converts the problem into a **range sum query problem**.

---

### Step 2: Build Prefix Sum Array

Construct a prefix sum array `ps` such that:

* `ps[i]` stores the number of valid words from index `0` to `i`

This allows us to answer range queries in **O(1)** time.

---

### Step 3: Answer Queries

For each query `[l, r]`:

* If `l == 0` → answer is `ps[r]`
* Else → answer is:

  ```
  ps[r] - ps[l - 1]
  ```

---

## ⏱ Complexity

* **Time Complexity:**

  * Building contribution array → `O(n)`
  * Prefix sum computation → `O(n)`
  * Answering queries → `O(q)`
    👉 Overall: **O(n + q)**

* **Space Complexity:**

  * Contribution array + prefix sum → **O(n)**

---

## 💻 Code

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)

        # Step 1: Contribution array
        contri = []
        for w in words:
            if w[0] in vowel and w[-1] in vowel:
                contri.append(1)
            else:
                contri.append(0)

        # Step 2: Prefix sum
        ps = [0] * n
        currSum = 0
        for i in range(n):
            currSum += contri[i]
            ps[i] = currSum

        # Step 3: Answer queries
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(ps[r])
            else:
                ans.append(ps[r] - ps[l - 1])

        return ans
```

---

## ⚠️ Common Mistakes

* ❌ Forgetting to handle `l == 0` case in prefix sum
* ❌ Incorrect prefix sum construction
* ❌ Using list instead of set for vowel lookup (slower)

---

## ✅ Key Takeaways

* Convert conditions into a **binary contribution array**
* Use **prefix sums** for efficient range queries
* This pattern is widely applicable in range-based problems

---




# 🧠 Revision Note: Maximum Number of Vowels in a Substring of Length K

**Question: LC 1456** https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
## 🪜 My Thought Progression (Very Important)
- Bad note: I took more than 1 hour to get to the optimize solution

### 🔴 Step 1: Brute Force (First Attempt)

* Idea: Check every substring of size `k`
* Count vowels each time

```python
sum(...) or countVowel(...)
```

⛔ Problem:

* Recomputing every window
* **Time:** `O(n × k)` → TLE

👉 ❗ Lesson:

> Avoid recomputing overlapping work

---

### 🟡 Step 2: Contribution + Prefix Sum

* Convert string → binary array (`1` if vowel)
* Use prefix sum to get range sum

✔️ Works in:

* **Time:** `O(n)`
* **Space:** `O(n)`

⚠️ Problem:

* Extra space unnecessary
* Overkill for fixed window

👉 ❗ Lesson:

> Prefix sum is useful for **multiple range queries**, not sliding windows

---

### 🟢 Step 3: Optimal — Sliding Window

💡 Key Idea:

> Don’t recompute → **update**

* Add new character
* Remove old character

---

## 🚀 Final Pattern

```python
count += (new char contribution)
count -= (old char contribution)
```

---

## ⚡ Final Code Template (Mental Model)

```python
# 1. Build first window
# 2. Slide window
#    - add right
#    - remove left
# 3. track max
```

---

## ⏱ Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## 🎯 Key Observations

* Window size is **fixed (k)**
* Overlapping windows → reuse previous computation
* Maximum possible answer = `k` → early exit possible

---

## ⚠️ Common Mistakes (You Faced 👇)

* ❌ Using `sum()` inside loop → still `O(nk)`
* ❌ Thinking prefix sum is always optimal
* ❌ Off-by-one in window (`k` size confusion)

---

## 🧩 Pattern Recognition Rule

👉 If you see:

> “Substring of fixed size k”

Immediately think:

> **Sliding Window (add/remove)**

---

## 🏁 Final Takeaway

> Optimization journey:

```
Brute Force → Prefix Sum → Sliding Window ✅
```

👉 Best solution = **Sliding Window with running count**

---




# 985. Sum of Even Numbers After Queries

## 1. Problem Summary

Given an array `nums` and queries `[val, index]`, for each query:

* Update: `nums[index] += val`
* Return the sum of even numbers after each update

---

## 2. Constraints Insight

* Only **one element changes per query**
* Recomputing full sum each time → inefficient

---

## 3. Naive Approach

### Idea

For each query:

* Update array
* Loop through entire array and sum even numbers

### Complexity

* Time: **O(n * q)** → TLE
* Space: O(1)

---

## 4. Optimized Approach (Key Idea)

Maintain a **running sum of even numbers**.

Instead of recomputing:

> Adjust only the affected element.

---

## 5. Algorithm

1. Initialize:

   ```python
   evenSum = sum(x for x in nums if x % 2 == 0)
   ```

2. For each query `(val, i)`:

   * If `nums[i]` is even → remove it from sum
   * Update: `nums[i] += val`
   * If updated value is even → add it to sum
   * Append result

---

## 6. Code

```python
class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        evenSum = sum(x for x in nums if x % 2 == 0)
        ans = []

        for val, i in queries:
            if nums[i] % 2 == 0:
                evenSum -= nums[i]

            nums[i] += val

            if nums[i] % 2 == 0:
                evenSum += nums[i]

            ans.append(evenSum)

        return ans
```

---

## 7. State Transition Cases

| Before | After | Action                |
| ------ | ----- | --------------------- |
| Even   | Even  | subtract old, add new |
| Even   | Odd   | subtract old          |
| Odd    | Even  | add new               |
| Odd    | Odd   | no change             |

---

## 8. Edge Cases

* Negative numbers → still valid
* Zero is even
* Must update `nums[i]` (common bug)

---

## 9. Complexity

* Time: **O(n + q)**
* Space: **O(1)**

---

## 10. Pattern Recognition

This is a classic:

> **Incremental Update Pattern**

Use when:

* Only small part of data changes
* Global value depends on entire structure

---

## 11. Generalization

Same idea applies to:

* Prefix sum updates
* Hashmap frequency tracking
* Sliding window problems
* Real-time aggregation systems

---

## 12. Key Takeaway

> Never recompute global state if only one element changes.

Update it incrementally.

---

## 13. Feynman Explanation

Instead of recalculating everything:

* Remove old value
* Add new value

Like updating total money after replacing one note.
