

# LeetCode 392 - Is Subsequence

🔗 **LeetCode Problem**: [Is Subsequence](https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75)


## Problem Statement

Given two strings `s` and `t`, check if `s` is a subsequence of `t`.

A **subsequence** of a string is a new string generated from the original string with some (or no) characters deleted, **without changing the relative order** of the remaining characters.

---

## Example

```
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: a → b → c are present in order in `t`
```

```
Input: s = "axc", t = "ahbgdc"
Output: false
Explanation: 'x' is not present in `t`
```

---

## Optimal Solution Approach

We use a **two-pointer technique**, where:

- We iterate through the string `t`
- We maintain a pointer `i` to track how many characters of `s` we’ve matched so far
- If `t[j] == s[i]`, we move the `i` pointer forward
- At the end, if `i == len(s)`, all characters of `s` were found in order in `t`


---

## Time and Space Complexity

- **Time Complexity:** O(n), where n is the length of `t`
- **Space Complexity:** O(1), constant extra space

---

## Notes

- This solution is efficient even for large inputs
- It avoids unnecessary slicing or searching which would increase time complexity
```
