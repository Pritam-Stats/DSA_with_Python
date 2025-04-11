# GFG20 Check if Strings are Rotations of Each Other

[Problem Link](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/check-if-strings-are-rotations-of-each-other-or-not-1587115620)

## 🧠 Problem Summary

Given two strings `s1` and `s2` of equal length, check if `s2` is a rotation of `s1`.  
Rotation means shifting characters from one end to the other (left or right).

## ✅ Approach

If `s2` is a rotation of `s1`, it will always be a **substring of `s1 + s1`**.  
Also, both strings must have the same length.

## 🧪 Example

```python
s1 = "abcd"
s2 = "cdab"
# True, because rotating "abcd" two times gives "cdab"
