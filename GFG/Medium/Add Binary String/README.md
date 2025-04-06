
# Add Binary Strings

## Problem Statement

Given two binary strings `s1` and `s2` consisting of only 0s and 1s, return their sum as a binary string. The input strings may contain leading zeros, but the output string must **not** have any leading zeros (except when the result is `"0"`).

---

## Approach & Explanation

This problem is a classic case of **two-pointer + carry simulation**, inspired by how we do manual addition. We start from the end (least significant bit) of both strings and simulate binary addition, managing the carry at each step.

### Key Concepts:

- Start from the end of both strings (`s1` and `s2`)
- Use a `carry` to store overflow from binary addition
- Compute the sum bit-by-bit
- Append the result in reverse, then reverse it at the end
- Strip leading zeros in the final result
- If all bits are zero, return `"0"`

---

## Pseudocode

```text
function addBinaryStrings(s1, s2):
    i ← length of s1 - 1
    j ← length of s2 - 1
    carry ← 0
    result ← empty list

    while i ≥ 0 or j ≥ 0 or carry ≠ 0:
        total ← carry
        if i ≥ 0:
            total += int(s1[i])
            i -= 1
        if j ≥ 0:
            total += int(s2[j])
            j -= 1

        result.append(total % 2)
        carry ← total // 2

    reverse(result)
    remove leading zeros
    if result is empty:
        return "0"
    return result as string
```

---

## C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

string addBinary(string s1, string s2) {
    int i = s1.size() - 1, j = s2.size() - 1;
    int carry = 0;
    string result = "";

    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) total += s1[i--] - '0';
        if (j >= 0) total += s2[j--] - '0';

        result += (total % 2) + '0';
        carry = total / 2;
    }

    reverse(result.begin(), result.end());

    // Remove leading zeros
    int pos = result.find_first_not_of('0');
    if (pos == string::npos) return "0";
    return result.substr(pos);
}
```

---

## Time & Space Complexity

| Type            | Complexity                 |
|-----------------|----------------------------|
| Time Complexity | **O(max(N, M))**           |
| Space Complexity| **O(max(N, M))** (for result string) |

Where `N` and `M` are the lengths of input strings `s1` and `s2`.

---

## Edge Cases Handled

- Input strings have leading zeros (e.g., `"0001" + "001"`).
- Result has leading zeros (e.g., `"0001" + "0001" = 0010"` → output `"10"`).
- Both strings are zeros (e.g., `"0000" + "0000"` → output `"0"`).
- Strings of different lengths.

---

