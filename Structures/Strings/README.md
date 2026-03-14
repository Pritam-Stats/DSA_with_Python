- [1. Convert to uppercase](#1-convert-to-uppercase)
- [2. Reverse a character array](#2-reverse-a-character-array)
- [3. Valid Palindrome](#3-valid-palindrome)
- [4. Anagrams](#4-anagrams)
- [5. Replace Character in a String — Key Concepts](#5-replace-character-in-a-string--key-concepts)
  - [5.1. Problem Idea](#51-problem-idea)
  - [5.2. Concepts Learned](#52-concepts-learned)
    - [5.2.1. Strings are Immutable in Python](#521-strings-are-immutable-in-python)
    - [5.2.2. Inefficient String Concatenation](#522-inefficient-string-concatenation)
      - [5.2.2.1. Time Complexity](#5221-time-complexity)
    - [5.2.3. Efficient String Construction (List + Join)](#523-efficient-string-construction-list--join)
      - [5.2.3.1. Time Complexity](#5231-time-complexity)
    - [5.2.4. Built-in String Replacement](#524-built-in-string-replacement)
      - [5.2.4.1. Time Complexity](#5241-time-complexity)
    - [5.2.5. Best Solution for This Problem](#525-best-solution-for-this-problem)
    - [5.2.6. Competitive Programming Trick](#526-competitive-programming-trick)
    - [5.2.7. Key Takeaways](#527-key-takeaways)
    - [5.2.8. Complexity Summary](#528-complexity-summary)
- [6. Determine if two problems can be made equal with 1 swap](#6-determine-if-two-problems-can-be-made-equal-with-1-swap)
- [7. LC 1657 - Determine if two strings are close](#7-lc-1657---determine-if-two-strings-are-close)
    - [7.0.1. Intuition](#701-intuition)
    - [7.0.2. Python solution](#702-python-solution)
  - [7.1. Why the frequency multiset condition is correct](#71-why-the-frequency-multiset-condition-is-correct)
  - [7.2. Complexity of the Counter + sort solution](#72-complexity-of-the-counter--sort-solution)
  - [7.3. Short revision notes for you](#73-short-revision-notes-for-you)
    - [7.3.1. 1657 Close Strings – Key conditions](#731-1657-close-strings--key-conditions)
    - [7.3.2. Standard Python template](#732-standard-python-template)
    - [7.3.3. Complexity](#733-complexity)

<h1>Problems on Strings</h1>

# 1. Convert to uppercase
- Builtin python string method is .upper().
- We implemented using, ordinal number representation (ASCII values) using ord() fn and chr fn.
# 2. Reverse a character array
- Two pointer
- Imp question: Do we need to use `st <= end` or `st < end`?
    <details>
    <summary>Answer</summary>
        There will be no difference of equal, 
        - in case of even size equal will never occur and
        - in case of odd size when st == end; swapping one element returns that only.
    </details>

# 3. Valid Palindrome
- Two pointer technique
- If st and end are not equal at any point return false
  - TC: O$(N)$

# 4. Anagrams
- Track count of the first word, prepare a count array
- check for the second array if the count have that, if count exists keep decreasing he count
  - TC: O$(N)$
- Another idea is to sort both the words.
  - TC: O$(N log_2 N)$ (Builtin merge sort)
---

# 5. Replace Character in a String — Key Concepts

## 5.1. Problem Idea

Given a string `s` and two characters `c1` and `c2`, replace **every occurrence of `c1` with `c2`** and print the resulting string. (Problem G CF Week 5 -Strings) [Link]()

Example:

```
Input
abacaba
a b

Output
bbbcbbb
```

---

## 5.2. Concepts Learned

### 5.2.1. Strings are Immutable in Python

Python strings **cannot be modified in-place**.

Example:

```python
s = "hello"
s[0] = "H"   # ❌ Error
```

Instead, Python creates a **new string** when modifications are made.

---

### 5.2.2. Inefficient String Concatenation

Building strings using `+=` inside a loop is slow.

Example:

```python
ans = ""
for ch in s:
    ans += ch
```

Each `+=` creates a **new string**, leading to **quadratic time complexity**.

#### 5.2.2.1. Time Complexity

```
O(n²)
```

This becomes slow when `|s|` is large (up to `10^6` in this problem).

---

### 5.2.3. Efficient String Construction (List + Join)

A better approach is:

1. Store characters in a list
2. Join them at the end

Example:

```python
ans = []
for ch in s:
    ans.append(ch)

result = "".join(ans)
```

#### 5.2.3.1. Time Complexity

```
O(n)
```

Appending to a list is **O(1)**.

---

### 5.2.4. Built-in String Replacement

Python provides an optimized method:

```python
s.replace(old, new)
```

Example:

```python
s = "abacaba"
print(s.replace("a", "b"))
```

Output:

```
bbbcbbb
```

#### 5.2.4.1. Time Complexity

```
O(n)
```

This method is implemented in **C internally**, making it very fast.

---

### 5.2.5. Best Solution for This Problem

```python
s = input().strip()
c1, c2 = input().split()

print(s.replace(c1, c2))
```

---

### 5.2.6. Competitive Programming Trick

The entire solution can be written in **one line**:

```python
print(input().strip().replace(*input().split()))
```

---

### 5.2.7. Key Takeaways

* Python strings are **immutable**
* Avoid **string concatenation inside loops**
* Prefer **list + join** or **built-in string methods**
* Built-in functions like `replace()` are **highly optimized**

---

### 5.2.8. Complexity Summary

| Method                      | Time Complexity |
| --------------------------- | --------------- |
| String concatenation (`+=`) | O(n²)           |
| List + join                 | O(n)            |
| `str.replace()`             | O(n)            |

✔ Recommended approach: **use `replace()`**

---

# 6. Determine if two problems can be made equal with 1 swap
[Code](/06-determine-if-one-swap-can-make-two-words-equal.py)
- I found it difficult

Next Leetcode problem is related but not same

# 7. LC 1657 - Determine if two strings are close
[Link](https://leetcode.com/problems/determine-if-two-strings-are-close/description/)

For LeetCode **1657. Determine if Two Strings Are Close**, two strings are “close” if you can make one from the other using:  
1) swaps of any characters, and 2) changing all occurrences of one existing character into another existing character (and vice versa). [leetcode](https://leetcode.com/problems/determine-if-two-strings-are-close/)

Because you can reorder characters freely, position does not matter. The key facts are: [algo](https://algo.monster/liteproblems/1657)

- Both strings must use the **same set of characters**.  
- Their **multiset of frequencies** must match (when you sort the counts). [youtube](https://www.youtube.com/watch?v=2darQnsmjMs)

### 7.0.1. Intuition

- Operation 1 (swap) lets you rearrange characters arbitrarily, so only counts matter, not indices. [algo](https://algo.monster/liteproblems/1657)
- Operation 2 lets you rename characters but only among those that already exist. So the inventory of unique characters must stay the same, and the multiset of counts (like `[1,2,3]`) must be the same, even if attached to different letters. [youtube](https://www.youtube.com/watch?v=2darQnsmjMs)

Example:  
- `word1 = "aabccc"` → frequencies `{a:2, b:1, c:3}` → sorted counts `[1,2,3]`.  
- `word2 = "ccbaac"` → `{c:3, b:1, a:2}` → `[1,2,3]`.  
Same character set `{a,b,c}` and same sorted counts, so they are close. [algo](https://algo.monster/liteproblems/1657)

### 7.0.2. [Python solution](/07-lc-1657.py)

Simplest is to use `collections.Counter`:


- Time complexity: O(n log n) because of sorting the frequency lists, with n = length of string (practically near O(n) since there are at most 26 letters). [youtube](https://www.youtube.com/watch?v=2darQnsmjMs)
- Space complexity: O(1) or O(26) for lowercase letters, effectively constant. [github](https://github.com/doocs/leetcode/blob/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md)

---

Your dictionary‑and‑compare idea is exactly the **right invariant** for this problem; you were on the correct track. The difficulty is convincing yourself that the frequency condition is both **necessary and sufficient**.

***

## 7.1. Why the frequency multiset condition is correct

We have two operations: [algo](https://algo.monster/liteproblems/1657)

1. Swap any two positions → only reorders characters, does not change counts.  
2. Convert all occurrences of one character to another existing character (and vice versa) → this **permutes counts among letters**, but never changes the multiset of counts. [cnblogs](https://www.cnblogs.com/johnnyzhao/p/13977417.html)

So:

- If you start with counts e.g. `{a: 1, b: 2, c: 3}`, operation 2 can only ever give you **some relabeling** of these counts: `{x:1, y:2, z:3}` in any assignment. [algo](https://algo.monster/liteproblems/1657)
- Therefore the sorted list of counts (here `[1,2,3]`) is an **invariant** of all allowed operations. [cnblogs](https://www.cnblogs.com/johnnyzhao/p/13977417.html)

That proves:  

- **Necessity:** If two strings are close, after applying operations their counts multiset must match, so initially their sorted frequencies must be equal.  
- **Sufficiency:** If both the character set and sorted frequency multiset match, you can always rename characters to match the target counts, then swap to fix order. [leetcode](https://leetcode.com/problems/determine-if-two-strings-are-close/)
  - Each frequency value in one string can be assigned to some character with the same frequency in the other string; operation 2 lets you perform these renamings; operation 1 then reorders.

This is why your dry run “felt right”: you had found the invariant but hadn’t formalized the **only if / if** reasoning.

***

## 7.2. Complexity of the Counter + sort solution

For lowercase English letters only (26 letters): [github](https://github.com/doocs/leetcode/blob/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md)

- Building two `Counter`s:  
  - Each is O(n) time, O(1) space (26 buckets max).  
- `set(c1.keys())` and `set(c2.keys())`:  
  - At most 26 elements → O(1) time and space.  
- Sorting `c1.values()` and `c2.values()`:  
  - At most 26 integers each → technically O(26 log 26), i.e., **O(1)** in practice.  

So under the real constraints the algorithm is **O(n)** time and **O(1)** extra space. [github](https://github.com/doocs/leetcode/blob/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md)

Your mental formula “Counter O(n) + sort O(n log n) → O(n + n log n)” is correct in a general alphabet, but for fixed‑size alphabets like lowercase letters, sort is constant‑time. So both viewpoints are fine; in interviews you usually say **O(n)**.

***

## 7.3. Short revision notes for you

Use this as a quick checklist before/after coding.

### 7.3.1. 1657 Close Strings – Key conditions

- Two strings are **close** if:  
  - You can reorder letters arbitrarily (swaps), and  
  - You can rename letters among existing characters (global swap of all `x` and `y`). [leetcode](https://leetcode.com/problems/determine-if-two-strings-are-close/)

To be close:

1. **Same length**  
   - Otherwise impossible to match.  

2. **Same character set**  
   - `set(word1) == set(word2)` must hold.  
   - Because operation 2 cannot introduce a completely new character or remove all of a character; it only swaps labels among already present characters. [algo](https://algo.monster/liteproblems/1657)

3. **Same multiset of frequencies**  
   - Build frequency maps: `Counter(word1)`, `Counter(word2)`.  
   - Check `sorted(c1.values()) == sorted(c2.values())`.  
   - Reason: operations only **permute** which letter has which count; they never change the bag of counts. [cnblogs](https://www.cnblogs.com/johnnyzhao/p/13977417.html)

### 7.3.2. Standard Python template

```python
from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    c1, c2 = Counter(word1), Counter(word2)

    if set(c1.keys()) != set(c2.keys()):
        return False

    return sorted(c1.values()) == sorted(c2.values())
```

### 7.3.3. Complexity

- Building counters: O(n) time.  
- Sorting counts:  
  - General alphabet: O(m log m) where m = number of distinct chars.  
  - LeetCode (26 lowercase letters): m ≤ 26 ⇒ treat as O(1).  
- Overall: **O(n)** time, **O(1)** extra space for this problem. [github](https://github.com/doocs/leetcode/blob/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close/README_EN.md)

***

When you get an intuition like “compare count dictionaries”, try to **name the invariant** (“sorted frequency multiset does not change under operations”) and then argue necessity and sufficiency. That’s the step that turns a gut feeling into a proof.


