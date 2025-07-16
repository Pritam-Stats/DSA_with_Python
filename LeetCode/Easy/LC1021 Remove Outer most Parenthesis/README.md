- **Problem Link** : [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/description/)
- **Date** : July 17, 2025
- **Topic** : [[String]]
- **Difficulty** : #Easy 

---
### Summary Description: 
- Given a string of parenthesis. We have to remove the outermost.
- A valid parentheses string is either:`"()"`, or a concatenation of two valid parentheses strings, or a valid parentheses string wrapped with a pair of parentheses.
</br>
Given a valid parentheses string `s`, **remove the outermost parentheses of every primitive string** in the primitive decomposition of `s`. </br>
A **primitive string** is a nonempty valid parentheses string that **cannot be broken** into two non-empty valid parentheses strings.

`s = "(()())(())"  ->   "()()()"` 
## Strategy & Key Insights
- Use a Stack like approach.
- Primitive decompositions: `"(()())"` and `"(())"`
- Removing outermost parentheses: `"()()"` and `"()"` → combined → `"()()()"`
##### Approach (Stack Depth Tracking):
- We track the **depth** of the parentheses to find **outermost ones**.
- We can iterate through the string and use a `count` variable (like a stack size):
- When we see `'('`, if `count > 0` → it's not outermost → add to result. Then increment `count`.
- When we see `')'`, decrement `count` first. If `count > 0` → it's not outermost → add to result.
---
#### Key Observations:

1. **Single-pass** solution: Iterates the input string **once**  => optimal time.
2. **No stack needed**: `count` acts like a depth tracker => avoids actual stack overhead => efficient.
3. **Minimal space usage**: Apart from the output string, uses O(1) auxiliary space => space-optimal.

##### Time and Space Complexity:

- **Time:** O(n) — one pass through the string of length `n`.
- **Space:** O(n) — for the result string (unavoidable, since we must output something).

---

#### Is there a Better Solution? 

- **Time**: We **must** read each character at least once.
	- cannot do better than O(n).
- **Space**: We must **store** the result. 
	- output string will be size O(n) in worst case (if every paren is inner).
---
