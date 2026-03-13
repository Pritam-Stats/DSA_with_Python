- [1. Convert to uppercase](#1-convert-to-uppercase)
- [2. Reverse a character array](#2-reverse-a-character-array)
- [3. Valid Palindrome](#3-valid-palindrome)
- [4. Anagrams](#4-anagrams)

<h1>Problems on Strings</h1>

# 1. Convert to uppercase
- Builtin python string method is .upper().
- We implemented using, ordinal number representation (ASCII values) using ord() fn and chr fn.
# 2. Reverse a character array
- Two pointer
- Imp question: Do we need to use `st <= end` or `st < end`?
    <details>
    <summary>Answer</summary>
        There will be no difference of equal, 
        - in case of even size equal will never occur and
        - in case of odd size when st == end; swapping one element returns that only.
    </details>

# 3. Valid Palindrome
- Two pointer technique
- If st and end are not equal at any point return false
  - TC: O$(N)$

# 4. Anagrams
- Track count of the first word, prepare a count array
- check for the second array if the count have that, if count exists keep decreasing he count
  - TC: O$(N)$
- Another idea is to sort both the words.
  - TC: O$(N log_2 N)$ (Builtin merge sort)