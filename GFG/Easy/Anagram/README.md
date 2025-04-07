# Anagram Checker - 16 of GFG160

This program checks whether two given strings are **anagrams** of each other or not.

🔗 **GFG Problem**: [Anagram](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620)

---

### 🔍 What is an Anagram?
Two strings are anagrams if they contain the **same characters** in **any order**, with the **same frequency**.  
Example: `"listen"` and `"silent"` are anagrams.

---

## ✅ Logic Used

1. **Length Check**: If lengths of both strings are different, they can’t be anagrams.
2. **Frequency Count**:
   - Create a dictionary (`freq`) to count characters in the first string.
   - For each character in the second string, decrement the corresponding count.
3. **Final Check**: If all values in `freq` are `0`, the strings are anagrams.

---

## ⏱️ Time & Space Complexity

| Metric         | Value       |
|----------------|-------------|
| **Time**       | `O(n)`      |
| **Space**      | `O(1)` *(because max 26 lowercase letters)* |

---

### CPP Version
```
#include <iostream>
#include <unordered_map>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length())
        return false;

    unordered_map<char, int> freq;

    for (char c : s)
        freq[c]++;

    for (char c : t)
        freq[c]--;

    for (auto& entry : freq)
        if (entry.second != 0)
            return false;

    return true;
}

int main() {
    cout << boolalpha;
    cout << isAnagram("geeks", "kseeg") << endl;     // true
    cout << isAnagram("listen", "silent") << endl;   // true
    cout << isAnagram("hello", "bello") << endl;     // false
    return 0;
}
```
