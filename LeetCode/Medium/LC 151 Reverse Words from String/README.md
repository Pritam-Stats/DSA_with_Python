# Reverse Words in a String

🔗 [LeetCode Problem 151 - Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75)

---

## 🧠 Problem Statement

Given a string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words are separated by at least one space.

You must:
- Reverse the words (not characters) in the string
- Remove leading, trailing, and extra spaces
- Return a string with words joined by a single space

### Example:

Input: " the sky is blue " Output: "blue is sky the"


---

## ✅ Constraints

- `1 <= s.length <= 10⁴`
- The string may contain:
  - English letters (upper and lowercase)
  - Digits
  - Spaces
- At least one word will be present

---

## 🧩 Approach (Manual / DSA-Friendly)

To solve this efficiently without relying on built-in functions like `.split()` or `.strip()`, we simulate the reverse operation manually by scanning the string **from right to left**.

### Core Logic:

1. **Start from the end** of the string.
2. **Skip any trailing or extra spaces** between words.
3. **Identify a word** (bounded by non-space characters).
4. **Append the word** to a result list.
5. Repeat until the entire string is processed.
6. **Join the words with a single space**.

This approach avoids extra processing and keeps the time complexity linear.

---

## 🧱 Pseudocode

```
Initialize empty result list Set i = length of string - 1

While i >= 0: Skip spaces while i >= 0 and s[i] == ' '
If i < 0: break (end of string)

Set j = i
While j >= 0 and s[j] != ' ':
    j -= 1  (find beginning of the word)

Append substring s[j+1 to i+1] to result
Set i = j - 1  (move to the next word)

Join the result list using a single space Return the final string
```



---

## 🧑‍💻 C++ Implementation

```cpp
class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        int i = s.length() - 1;

        while (i >= 0) {
            // Skip trailing and extra spaces
            while (i >= 0 && s[i] == ' ') i--;
            if (i < 0) break;

            int j = i;
            // Find start of the word
            while (j >= 0 && s[j] != ' ') j--;

            // Extract the word and add to result
            words.push_back(s.substr(j + 1, i - j));
            i = j - 1;
        }

        // Join the words with a single space
        string result;
        for (int k = 0; k < words.size(); ++k) {
            result += words[k];
            if (k != words.size() - 1)
                result += ' ';
        }

        return result;
    }
};
```

## Key Points
- Handles leading, trailing, and multiple spaces manually.

- No extra dependencies or built-in string split helpers.

- Efficient and interview-friendly.

## Time & Space Complexity:
- Time: O(n) — each character is visited once

- Space: O(n) — for storing words in the reversed order

#### Edge Cases
- Input with only spaces → should return an empty string

- Input with single word → should return the same word

- Input with multiple spaces between words → should be reduced to one space between words