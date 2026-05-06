# Bit Manipulation – Competitive Programming Revision Notes

---

## Single Number 2 LC 137

#### To understand why we subtract at the 31st bit, 
- we have to look at how computers represent negative numbers using Two's Complement.

##### 1. The 32nd Bit (The Sign Bit)
    
- In a standard 32-bit signed integer, the bits are not all "positive." The first 31 bits (index 0 to 30) represent positive powers of 2. However, the 31st bit (the Most Significant Bit) represents -2^{31}.
    
- If the 31st bit is 0, the number is positive.
- If the 31st bit is 1, you add -2,147,483,648 to the sum of the other bits.
  
##### 2. Why we subtract in Python
- Python is unique because its integers don't have a fixed size (they don't "overflow" at 32 bits). If we simply did ans |= (1 << 31), Python would treat that as adding +2^{31}, resulting in a large positive number (2,147,483,648) instead of the negative version.

- By using if j == 31: ans -= (1 << 31), we are manually telling Python: "Hey, if this bit is set, it's actually the sign bit, so treat it as a negative value."

##### A Simple 4-bit Example
- Imagine we are working with 4-bit signed integers instead of 32-bit.

- The bits represent: -2^3, 2^2, 2^1, 2^0 (which is -8, 4, 2, 1).
    
    If our "single number" is -3, its binary representation in 4-bit Two's Complement is 1101.
- Let's see how our code reconstructs it:

| Bit Position ($j$) | Binary Weight | Bit Present in -3? | `colSum % 3 != 0` | Action | Resulting `ans` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | $2^0 = 1$ | **Yes** (1) | True | `ans += 1` | 1 |
| **1** | $2^1 = 2$ | **No** (0) | False | None | 1 |
| **2** | $2^2 = 4$ | **Yes** (1) | True | `ans += 4` | 5 |
| **3 (Sign)** | $-2^3 = -8$ | **Yes** (1) | True | `ans -= 8` | **-3** |



- If we hadn't treated the 3rd bit as negative, we would have done 5 + 8 = 13. In a 32-bit environment, that's the difference between getting the correct negative answer and a massive positive one.
##### Summary of the Logic
- Bits 0-30: These are positive. We use ans |= (1 << j) to add them up.
- Bit 31: This is the "negative weight." If the logic determines the single number has this bit, we subtract it from our total to shift the number into the negative range.
Does seeing that 4-bit table help visualize how the sign bit "pulls" the positive sum into a negative value?













---

## Binary Basics

- Representation: integers stored in binary (base-2)
- Bit positions: 0-indexed from LSB (rightmost)
- Bit length:
    - bits(n) = floor(log2(n)) + 1

---

## Core Bitwise Operators

Operator	Name	Behavior
```
    `&`	AND	1 only if both bits are 1
    `|`	OR
    `^`	XOR	1 if bits differ
    `~`	NOT	flips all bits (two’s complement)
    `<<` Left shift	multiply by 2^k
    `>>` Right shift	divide by 2^k (floor)
```

---

## Powers of Two

- Generate:

```py
1 << k   # 2^k
```

- Check if power of two:

```py
n > 0 and (n & (n - 1)) == 0
```

- Remove lowest set bit:

```py
n & (n - 1)
```

- Isolate lowest set bit:

```py
n & -n
```

- Highest power of 2 ≤ n:

```py
    1 << (n.bit_length() - 1)
```

---
## Bit Operations on Index i

- Check bit:
```py
(n >> i) & 1
```

- Set bit:
```py
n | (1 << i)
```
- Clear bit:
```py
n & ~(1 << i)
```
- Toggle bit:
```py
n ^ (1 << i)
```
---
## Counting Bits

- Builtin:
    ```py
    n.bit_count()
    ```
- Brian Kernighan:
    ```py
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    ```
- Complexity: O(number of set bits)

---
## XOR Properties (Very Important)

- `a ^ a = 0`
- `a ^ 0 = a`
- Commutative and associative

Applications:

- Find unique element (others appear twice)
- Prefix XOR

---
## Subsets using Bitmask

- Iterate all subsets of size n:
    ```py
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                pass
    ```py
- Submask iteration:
    ```py
    sub = mask
    while sub:
        sub = (sub - 1) & mask
    ```
- Complexity: O(2^n)

---
## Bitmask DP (Pattern)

- State: dp[mask]
- Transition: remove or add bits

Example idea:

- Traveling Salesman (TSP)
- Assignment problems

---
## Tricks and Identities

- Addition using bits: `A + B = (A ^ B) + ((A & B) << 1)`

- Negation (Two’s Complement): `-n = ~n + 1`

- Check opposite signs: `(a ^ b) < 0`

- **Swap without temp**
    ```py
    a ^= b
    b ^= a
    a ^= b
    ```
---

## Range Tricks

- XOR from 1 to n:
    ```py
    def xor_1_to_n(n):
        return [n, 1, n+1, 0][n % 4]
    ```
- Range XOR:
    ```py
    xor(l, r) = xor_1_to_n(r) ^ xor_1_to_n(l-1)
    ```
---

## Bitwise Greedy Patterns

- Maximize XOR → try setting highest bits first
- Trie (binary trie) for XOR queries

---
##  Common Problems Mapping

- Single number → XOR
- Two unique numbers → XOR + partition by set bit
- Missing number → XOR / sum formula
- Subset generation → bitmask
- Maximum XOR pair → trie

---

## Complexity

- Bitwise ops: O(1)
- Loop over bits: O(log n)
- Subsets: O(2^n)

---

## Pitfalls

- Negative numbers behave differently due to infinite sign extension
- Right shift of negative numbers is implementation-dependent in some languages
- Overflow in C++ (use long long)

---
