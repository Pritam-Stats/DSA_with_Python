# Problems
1. Convert to uppercase
    - Builtin python string method is .upper().
    - We implemented using, ordinal number representation (ASCII values) using ord() fn and chr fn.
2. Reverse a character array
    - Two pointer
    - Imp question: Do we need to use `st <= end` or `st < end`?
        <details>
        <summary>Answer</summary>
            There will be no difference of equal, 
            - in case of even size equal will never occur and
            - in case of odd size when st == end; swapping one element returns that only.
        </details>