# Palindrome LC-125

Concepts: String, regex
Difficulty: Easy
Mark Done: Yes
Problem Link: https://leetcode.com/problems/valid-palindrome/description/
Solved Date: March 7, 2025

# Palindrome

## Question:

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

- **Input-Output Example:**
  **Example 1:**
  ```
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.

  ```
  **Example 2:**
  ```
  Input: s = "race a car"
  Output: false
  Explanation: "raceacar" is not a palindrome.

  ```
  **Example 3:**
  ```
  Input: s = " "
  Output: true
  Explanation: s is an empty string "" after removing non-alphanumeric characters.
  Since an empty string reads the same forward and backward, it is a palindrome.
  ```
  **Example 4:**
  ```
  Input: s = "ab_a"
  Output: true
  Explanation: have to remove _
  ```

## Solution:

Step 1: Remove all the alphanumeric characters

Step 2: make all the char lower

Step 3: Check if the reverse is same

# Approach 1: Using regex and slicing

Using the substitute method in regular expression library

```python
def isPalindrome(s: str) -> bool:
    #we have to remove all alpha numeric character
    # we can use regex substitute
    import re
    cleaned_s = re.sub(pattern = r'[^a-zA-Z0-9]', repl = "", string = s).lower()

    return True if cleaned_s == cleaned_s[::-1] else False

print(isPalindrome(s = "race a car"))
```

### Explanation:

sub = substitute

- **pattern** takes the element we want to look for, to match. Here in the pattern argument, “r” method is to treat all the chars of the string in regular form, like in python backslash is used for new line or tab (\n,\t). this r method helps to avoid that.
  - “^” this is for **negation**. so pattern is searching for everything other than a to z, A-Z and numeric.
- And **repl** is to replace the pattern with something else, here we are just removing. and at the end lower() is to make all the letters small.
- Then we have used **string slicing** method to check if the reverse string is same as the original string.

**TC = O(n)**

**SC = O(n)**

# Approach 2: Two Pointers. Improving SC

**For a palindrome string, every corresponding char on the opposite side will be same.**

```python
def isPalindrome2(s: str) -> bool:
    # two pointer approach
    n = len(s)
    left, right = 0, n-1

    while left < right :
        # skips the non alpha numerics and update the pointers
        # below we will check for false. imagine we already assumed that it's Palindrome
        while left<right and not s[left].isalnum():
            left += 1
        while left<right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower(): #return False if any char doesn't match
            return False
        # update to check the next pair of chars
        left += 1
        right -=1

    return True
```
