
# 🧠 Minimum Characters to Make a String Palindrome (Front Insertion)

This project solves the problem of finding the **minimum number of characters to add at the beginning** of a given string `s` so that the resulting string becomes a **palindrome**.

---

🔗 [GFG19 - Minimum Characters to Add to make a Palindrome](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/minimum-characters-to-be-added-at-front-to-make-string-palindrome)

## 📂 Files

- `Brute_Force.py`: Naive approach using repeated prefix checks.
- `Optimal_KMP.py`: Optimized solution using the **KMP prefix function (LPS array)**.

---

## 📝 Problem Statement

Given a string `s`, determine the **minimum number of characters** that must be **added to the front** of the string to make it a **palindrome**.

---

## 🔁 Brute Force Approach (`Brute_force.py`)

### 🔍 Logic

- The idea is to find the **longest palindromic prefix** of the string.
- Starting from the full string and reducing the right end character-by-character, we keep checking if the current substring is a palindrome.
- The number of characters to be added = total length − length of longest palindromic prefix.

### 🧠 How it works

1. Start from the full string.
2. Check if substring `s[0..i]` is a palindrome.
3. If not, reduce `i` and repeat.
4. Once you find the longest palindromic prefix, subtract its length from total length to get the answer.

### 🕒 Time Complexity

- Checking if a string is palindrome takes O(n) time.
- We might check up to `n` prefixes.
- **Total time complexity**: `O(n^2)`

### ✅ Space Complexity

- `O(1)` (only using a few pointers).

---

## ⚡ Optimal KMP-based Approach (`Optimal_KMP.py`)

### 🚀 Core Idea

This approach is based on the **LPS (Longest Prefix Suffix)** array from the **KMP string matching algorithm**.

We reverse the string and append it to the original string with a separator:
```python
combined = s + '$' + reverse(s)
```

The goal is to find the **longest palindromic prefix**, which is equivalent to finding the **longest suffix of the reversed string that matches the prefix of the original**.

### 🔁 Steps

1. Reverse the original string.
2. Create a combined string as: `original + '$' + reversed`.
3. Build the LPS array for this combined string.
4. The **last value of the LPS array** gives the **length of the longest prefix** which is also a suffix — i.e., the longest palindromic prefix.
5. Subtract that length from the total to get the minimum characters to add.

### 📘 Why `$`?
The `$` is a delimiter that **never occurs** in the string. It ensures that no false overlaps occur between the original and reversed string.

### 🧠 LPS Array Insight

- `lps[i]` stores the length of the **longest prefix which is also a suffix** for the substring `s[0..i]`.
- When building the LPS array:
  - On a match, extend the prefix-suffix.
  - On a mismatch, use `lps[length - 1]` to jump to a smaller matching prefix instead of restarting — which keeps the algorithm efficient.

### 🕒 Time Complexity

- Building the LPS array is **O(n)**.
- Reversal and combining are **O(n)**.
- **Total time complexity**: `O(n)`

### ✅ Space Complexity

- `O(n)` for the LPS array and combined string.

---

## 📊 Summary of Approaches

| Approach       | Time Complexity | Space Complexity | Notes                         |
|----------------|------------------|-------------------|-------------------------------|
| Brute Force    | O(n²)           | O(1)              | Simple but inefficient        |
| KMP-based LPS  | O(n)            | O(n)              | Fast and optimal using KMP    |

---

## 📌 Final Note

The KMP-based solution is highly recommended for large strings due to its linear time efficiency, while the brute-force method is useful for understanding the problem's fundamentals.

```

