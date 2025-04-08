# Day 17 of GFG160

🔗 **GFG Problem**: [Non Repeating Character](https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/non-repeating-character-1587115620)

# First Non-Repeating Character in a String

Given a string consisting of only lowercase English letters, the task is to find the **first non-repeating character**. If no such character exists, return `$`.

This document explains three different approaches to solving the problem:

---

## 🧪 1. Brute Force Approach

### 🔹 Logic:
- Loop through each character in the string.
- For each character, loop through the entire string again to check if it occurs more than once.
- Return the first character that has no duplicates.

### ⏱️ Time & Space:
- **Time Complexity:** O(N²), due to the nested loop.
- **Space Complexity:** O(1), no extra space is used.

### ❌ Downsides:
- Very inefficient for long strings.
- Not recommended in coding interviews or large input cases.

---

## 🧠 2. Optimal Pythonic Approach (Using Dictionary)

### 🔹 Logic:
- Use a dictionary to store character frequencies.
- Traverse the string once to build the frequency dictionary.
- Then traverse the string again to find the first character with a frequency of 1.

### 🔧 Key Python Feature Used:
- `dict.get(key, default)` — returns the value for `key` if it exists, otherwise returns `default`. Helps increment counts concisely:
  ```python
  freq[ch] = freq.get(ch, 0) + 1
  ```

### ⏱️ Time & Space:
- **Time Complexity:** O(N)
- **Space Complexity:** O(1) — since there are only 26 lowercase letters.

### ✅ Advantages:
- Very readable and concise in Python.
- Ideal for Python-specific implementations.

---

## 🚀 3. Optimal Language-Agnostic Approach (Using Fixed Array)

### 🔹 Logic:
- Use a fixed-size array (size 26) to count character frequencies.
- Map each character to an index using its position in the alphabet.
- Traverse the string once to populate the frequency array.
- Traverse the string again to find the first character with frequency 1.

### 🧮 Key Concept:
- Use the ASCII value of a character to map it to an index:
  ```python
  index = ord(ch) - ord('a')
  ```
  - `ord(ch)` gives the Unicode/ASCII integer value of the character.
  - Subtracting `ord('a')` gives a value between 0 and 25 for lowercase letters.

### ⏱️ Time & Space:
- **Time Complexity:** O(N)
- **Space Complexity:** O(1) — fixed array of size 26.

### 🌍 Language-Agnostic Benefits:
- Works efficiently and similarly in most languages (C++, Java, etc.).
- No dependence on high-level data structures like dictionaries.

---

## ✅ Summary Comparison

| Approach               | Time Complexity | Space Complexity | Notes                             |
|------------------------|------------------|-------------------|------------------------------------|
| Brute Force            | O(N²)           | O(1)              | Inefficient                        |
| Pythonic Dict Approach | O(N)            | O(1)              | Clean and concise in Python        |
| Array-Based Approach   | O(N)            | O(1)              | Fast and works in any language     |

---



```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    char nonRepeatingChar(string s) {
        // Create an array of size 26 to store the frequency of each character
        vector<int> freq(26, 0);

        // Traverse the string to count the frequency of each character
        for (char ch : s) {
            freq[ch - 'a']++;
        }

        // Traverse the string again to find the first non-repeating character
        for (char ch : s) {
            if (freq[ch - 'a'] == 1) {
                return ch;  // First non-repeating character
            }
        }

        return '$';  // If no non-repeating character exists
    }
};

int main() {
    Solution solution;
    string s = "geeksforgeeks";
    char result = solution.nonRepeatingChar(s);
    
    if (result != '$') {
        cout << "First non-repeating character: " << result << endl;
    } else {
        cout << "No non-repeating character found." << endl;
    }

    return 0;
}
```

### 🔍 Explanation:
- **Frequency Array:** We use a `vector<int> freq(26, 0)` to store the frequency of each lowercase letter.
  - The index of the array corresponds to the letter: `freq[ch - 'a']` for a character `ch`.
- **First Pass (Counting):** The first loop goes through the string and counts the occurrences of each character.
- **Second Pass (Finding Non-Repeating):** The second loop checks the original string and finds the first character whose count is 1.
- If no non-repeating character is found, it returns `'$'`.

### 🚀 Time & Space Complexity:
- **Time Complexity:** O(N), where N is the length of the string.
- **Space Complexity:** O(1) — only a fixed-size array of 26 is used.


---
This problem is a classic example of how frequency-counting and order-tracking can be combined efficiently using the right data structure.
```
