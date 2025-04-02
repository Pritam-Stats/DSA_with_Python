# LeetCode 1071: Greatest Common Divisor of Strings

## Problem Statement
Given two strings `str1` and `str2`, return the largest string `X` such that both `str1` and `str2` are formed by repeating `X` some number of times.
---
> Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
---
## Approach 1: Using Python's `math.gcd()`
- The greatest common divisor (GCD) of the lengths of `str1` and `str2` determines the length of the largest possible repeating substring.
- If `str1 + str2` is not equal to `str2 + str1`, then no valid repeating substring exists.
- The answer is `str1[:gcd(len(str1), len(str2))]`.

## Approach 2: Using the Euclidean Algorithm
- Instead of relying on `math.gcd()`, we can compute the GCD manually using the Euclidean algorithm.
- The Euclidean algorithm repeatedly applies `gcd(a, b) = gcd(b, a % b)` until `b` becomes `0`.
- The first `gcd_length` characters of `str1` will be our answer.

## Dry Run Examples
### Example 1:
**Input:**
```
str1 = "ABCABC", str2 = "ABC"
```
**Stepwise Execution:**
1. `str1 + str2 = "ABCABCABC"`, `str2 + str1 = "ABCABCABC"` → ✅ Matches
2. Compute `gcd(6, 3) = 3`
3. Return `str1[:3] = "ABC"`

**Output:** `"ABC"`

### Example 2:
**Input:**
```
str1 = "LEET", str2 = "CODE"
```
**Stepwise Execution:**
1. `str1 + str2 = "LEETCODE"`, `str2 + str1 = "CODELEET"` → ❌ Does not match
2. Return `""` (no common divisor string)

**Output:** `""`

## Complexity Analysis
- **Concatenation Check:** `O(N + M)`
- **GCD Computation (Euclidean Algorithm):** `O(log(min(N, M)))`
- **Returning Substring:** `O(K)`, where `K = gcd(N, M)`
- **Overall Complexity:** `O(N + M)`

