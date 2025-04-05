# Reverse Vowels of a String – LeetCode 345

🔗 [Problem Link](https://leetcode.com/problems/can-place-flowers/submissions/1596843160/?envType=study-plan-v2&envId=leetcode-75)

## 🧠 Problem Statement

Given a string `s`, reverse only the vowels of the string and return the resulting string.

### Example:
Input: "hello" → Output: "holle" Input: "leetcode" → Output: "leotcede"


---

## 🚀 Explanation of the Logic

### 1. Using Extra Space (Simple & Intuitive)

- **Approach**:
  - Traverse the string and collect all vowels in a list.
  - Reverse the list of vowels (using slicing or a loop).
  - Convert the original string into a list to modify it (since strings are immutable).
  - Traverse again and replace vowels in order with the reversed vowels.

- **Notes**:
  - Makes use of `s[i].lower()` to handle case-insensitive comparisons.
  - Reversal can be done with `present_vowels[::-1]` or a loop till `len // 2`.
  - This approach is very readable and good for beginners.
  
- **Time Complexity**: O(n)  
- **Space Complexity**: O(k), where k = number of vowels

---

### 2. Optimal Two-Pointer Approach (In-place)

- **Approach**:
  - Use two pointers, `left` and `right`, starting from both ends.
  - Move them toward each other until both point to vowels.
  - Swap the vowels in-place and continue moving.
  - Vowels are stored in a set for O(1) lookup.

- **Why It’s Better**:
  - Does not use any extra space to store vowels.
  - Faster and more memory efficient for large strings.
  - Still easy to understand with clear pointer logic.
  - String is not Mutable in Python unlike CPP, so we converted to list and used join method at the end

- **Time Complexity**: O(n)  
- **Space Complexity**: O(1)

---

## 💻 C++ Code (Optimal Two-Pointer Solution)

```cpp
class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        int left = 0, right = s.size() - 1;

        while (left < right) {
            while (left < right && vowels.find(s[left]) == vowels.end()) left++;
            while (left < right && vowels.find(s[right]) == vowels.end()) right--;
            swap(s[left], s[right]);
            left++;
            right--;
        }

        return s;
    }
};

