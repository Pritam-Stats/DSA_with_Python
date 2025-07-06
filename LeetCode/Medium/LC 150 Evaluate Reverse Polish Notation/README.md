- Problem Link: [LC 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
- Topic: **Stack**
- Level: *Medium*
- Date: *July 6th, 2025*
---

# Understanding Problem and the Approach


## 🧠 Understanding Postfix (Reverse Polish Notation)

In postfix notation:

* **Operators come after operands**
* No parentheses are needed

- Example:

```
Input: ["2", "1", "+", "3", "*"]
Means: (2 + 1) * 3 = 9
```

---

## Approach Using a Stack

1. Initialize an empty stack.
2. Traverse the tokens one by one.
3. If the token is a **number**, push it to the stack.
4. If the token is an **operator**:

   * Pop two operands from the stack.
   * Apply the operation: `operand2 op operand1` (note the order!)
   * Push the result back onto the stack.
5. At the end, the stack will have **one element**: the result.

---

### Division Edge case:

Python's integer division using `/` results in float.
Use `int(a / b)` to truncate **towards zero**, which is required.

Example:

* `int(5 / 2)` → `2`
* `int(-5 / 2)` → `-2` ✅ (correct)
* `-5 // 2` → `-3` ❌ (rounds toward negative infinity)



---

### 🔍 Example Test Case

- Input:

```
["4", "13", "5", "/", "+"]
```

- Explanation:

* "13 5 /" → 2
* "4 + 2" → 6

- Output:

```
6
```

---

## ⏱️ Time & Space Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

---


# The Essence of this problem
## 🔍 What is this problem really testing? (Chat GPT)

### 1. **Understanding Expression Evaluation Without Recursion or Infix**

Most people are comfortable with:

```python
3 + (4 * 5)
```

But **RPN/Postfix** expressions like:

```
3 4 5 * +
```

force you to evaluate expressions **without parentheses or precedence rules**.

This means you:

* Can’t rely on a parser or eval()
* Must **explicitly manage the expression structure** using **a stack**

👉 This is foundational to **compilers**, **interpreters**, and **virtual machines** (e.g., JVM bytecode).

---

### 2. **Mastery of the Stack as a Tool**

This problem is a **gold standard** test for whether you really understand **stacks**.

It tests:

* When and why to **push** or **pop**
* Preserving correct **order of operands**
* **Simulating call stacks / evaluation trees** in non-recursive ways

👉 Stacks are **everywhere**: parsing, backtracking, undo systems, tree traversals, etc.

---

### 3. **Operand Order + Division Behavior**

This is **very subtle** — many beginners **fail** on division:

```python
["10", "6", "/"] → 10 / 6 = 1 (truncate)
["-10", "6", "/"] → -10 / 6 = -1 (truncate toward zero)
```

You must:

* Preserve the **order** of operands (`a / b`, not `b / a`)
* Implement **rounding towards zero**, not floor division (`//` in Python)

👉 This tests attention to **edge cases** and **numerical behavior**, which often appear in real-world systems.

---

### 4. **Simulating Real-World Evaluation Engines**

Postfix notation is used in:

* **Stack-based virtual machines** (e.g., JVM, .NET CLR)
* **Compilers/interpreters** (RPN is a simplified way to represent code execution)
* **Spreadsheets**, calculators, etc.

When you evaluate postfix, you are essentially building a **mini virtual machine** that interprets bytecode-like instructions.

---

### 5. **Foundation for Harder Problems**

This simple-looking problem is a **building block** for more complex topics:

* Infix to Postfix conversion (Shunting Yard algorithm)
* Evaluating full expressions with variables/functions
* Building interpreters or parsers
* Implementing language syntax trees (ASTs)

---

## 🎓 So what is it *trying to teach*?

> **How to model expression evaluation explicitly using a stack**, instead of relying on language-level expression syntax or eval functions.

And in doing so:

* Teach precision with operand order
* Handle subtle math (like division rounding)
* Simulate real-world interpreters

---

## 🔥 Why it's labeled Medium

Not because it's *long* or *complicated* — but because:

* Many candidates **get operand order or division wrong**
* It requires **deep understanding of evaluation**, not just syntax
* It's easy to **assume it’s trivial**, and fail to handle edge cases

---


