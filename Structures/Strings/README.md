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

Given a string `s` and two characters `c1` and `c2`, replace **every occurrence of `c1` with `c2`** and print the resulting string.

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