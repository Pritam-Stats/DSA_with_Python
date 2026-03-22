# Foundation

This folder contains fundamental programming building blocks that strengthen core problem-solving ability before advanced DSA topics.

These problems are not primarily interview-focused.
They exist to improve control over logic, loops, recursion, and mathematical reasoning.

---

## Purpose of This Section

* Strengthen control over loops and conditionals
* Improve mathematical thinking
* Build comfort with recursion
* Develop number manipulation skills
* Master bit-level reasoning
* Improve implementation accuracy

Foundation work supports advanced data structures and algorithmic problem solving.

---

## Folder Structure


 - [Foundation](/Foundation/)
   - [Patterns](/Foundation/Patterns/)
   - [Mathematical-Problems](/Foundation/Mathematical-Problems/)
   - number_theory/
   - bit_manipulation/
   - recursion_basics/


---

## Topics Covered

### 1. Pattern Printing

Focus:

* Nested loops
* Index manipulation
* Logical construction of shapes
* Boundary handling

Skill Developed:
Precise control over iteration and condition flow.

---

### 2. Basic Math

Includes:

* GCD / LCM
* Prime checking
* Divisors
* Power calculations
* Digit manipulation
* Factorials

Skill Developed:
Mathematical modeling and numerical reasoning.

---

### 3. Number Theory (Introductory)

Includes:

* Sieve of Eratosthenes
* Modular arithmetic basics
* Fast exponentiation
* GCD properties

Skill Developed:
Efficiency thinking and mathematical optimization.

---

### 4. Bit Manipulation

Includes:

* XOR properties
* Set/clear/toggle bits
* Check power of 2
* Bit masking basics

Skill Developed:
Low-level logic optimization and constant-space tricks.

---

### 5. Recursion Basics

Includes:

* Basic recursive functions
* Recursion tree understanding
* Stack behavior visualization

Skill Developed:
Understanding function call stack and problem decomposition.

---

## Important Notes

* Keep solutions simple and clean.
* Avoid over-optimization here.
* Focus on correctness and clarity.
* Add short docstrings explaining logic.
* Do not turn this folder into advanced DSA practice.




## Count digits using logarithms $log_{10}$
This little snippet is a classic programmer's trick. In short: **it calculates the number of digits in a positive integer.**
[LC 1295](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) | [Code](/find-nums-with-even-digits.py)
```python
  class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if int(math.log10(num) + 1) % 2 == 0:
                cnt += 1
        return cnt
  ```
---

### How it Works (The Logic)

To understand why this works, we have to look at how logarithms relate to powers of 10:

* **$\log_{10}(10) = 1$**
* **$\log_{10}(100) = 2$**
* **$\log_{10}(1000) = 3$**

When you take the base-10 logarithm of a number, you are essentially finding out "10 to what power equals this number?"

1. **`math.log10(num)`**: This finds the magnitude. For a number like $450$, the log is approximately $2.65$.
2. **The "Invisible" Step**: Usually, this code is wrapped in a "floor" function or cast to an integer, like `int(math.log10(num))`. For $450$, this would turn $2.65$ into $2$.
3. **`+ 1`**: Since our count started at $2$ (representing the hundreds place), adding $1$ gives us $3$—the correct number of digits in $450$.

---

### Comparison: Math vs. Strings

Most beginners count digits by converting the number to text, but the math approach is often faster for the computer.

| Method | Example Code | Why use it? |
| --- | --- | --- |
| **String Method** | `len(str(num))` | Easy to read; handles any number format. |
| **Math Method** | `int(math.log10(num) + 1)` | **Performance.** It avoids allocating memory for a new string. |

---

### ⚠️ Two Important Notes

* **The "Zero" Error:** This function will crash (throw a `ValueError`) if `num` is $0$, because the logarithm of zero is undefined.
* **Negative Numbers:** This only works for positive integers. If you need to handle negatives, you’d use `math.log10(abs(num))`.
If the input num is 11, the function will return:$$\log_{10}(11) + 1 \approx 2.041392685158225$$
---

## Role in Overall Preparation

Foundation builds implementation strength.

Advanced problem solving happens in:

```
structures/
```

Foundation strengthens the base.
Structures develop interview mastery.

---

