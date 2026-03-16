- [1. Binary Number System](#1-binary-number-system)
    - [1.0.1. What is Decimal and Binary?](#101-what-is-decimal-and-binary)
  - [1.1. Decimal to Binary Conversion](#11-decimal-to-binary-conversion)
    - [1.1.1. Binary to Decimal](#111-binary-to-decimal)
- [2. Bit Manipulation](#2-bit-manipulation)
  - [2.1. Bitwise Operators](#21-bitwise-operators)
    - [2.1.1. And (\&) Operator](#211-and--operator)
    - [2.1.2. OR (|) -](#212-or---)
    - [2.1.3. XOR (^)](#213-xor-)
  - [2.2. Binary NOT](#22-binary-not)
  - [2.3. Binary **Shift** Operator](#23-binary-shift-operator)
- [3. Use of Bit Manipulation - in Problems](#3-use-of-bit-manipulation---in-problems)
  - [3.1. Check Power of 2](#31-check-power-of-2)
  - [3.2. Clear last i bits of a number](#32-clear-last-i-bits-of-a-number)
  - [3.3. Count Set Bits](#33-count-set-bits)
        - [3.3.0.0.1. Strategy](#33001-strategy)
- [4. Get Set Clear i-th Bit](#4-get-set-clear-i-th-bit)
    - [4.0.1. Set](#401-set)
  - [4.1. Check for Power of 2](#41-check-for-power-of-2)
          - [4.1.0.0.0.1. SO what will be the `4 & 3`](#410001-so-what-will-be-the-4--3)
      - [4.1.0.1. Why Does `n & (n - 1)` Remove the Rightmost Set Bit?](#4101-why-doesn--n---1remove-the-rightmost-set-bit)
      - [4.1.0.2. Algorithm Logic Step-by-Step](#4102-algorithm-logic-step-by-step)
- [5. One's Complement](#5-ones-complement)
- [6. Two's Complement](#6-twos-complement)
  - [6.1. Why Use Two’s Complement?](#61-why-use-twos-complement)
  - [6.2. How Does Two’s Complement Work?](#62-how-does-twos-complement-work)
  - [6.3. Example Table (8 bits)](#63-example-table-8-bits)
  - [6.4. How to Find Two’s Complement](#64-how-to-find-twos-complement)
    - [6.4.1. Explanation](#641-explanation)
    - [6.4.2. Bit Masking: `n & (2**bits - 1)`](#642-bit-masking-n--2bits---1)
        - [6.4.2.0.1. Formatting: `format(..., f'0{bits}b')`](#64201-formatting-format-f0bitsb)
        - [6.4.2.0.2. Summary Table](#64202-summary-table)
  - [6.5. Why is it Useful?](#65-why-is-it-useful)
  - [6.6. Quick Facts](#66-quick-facts)
- [7. Fast Exponentiation](#7-fast-exponentiation)
    - [7.0.1. Code Block](#701-code-block)


# 1. Binary Number System
### 1.0.1. What is Decimal and Binary?
- `Dec` means 10 and `Bi` means 2.
- In general number system and Mathematics we have 10 digits to form anything while in computer we only have 2 digits, 0 and 1. It's more a conventional with respect to electricity.
- 0 means there is no flow of current and 1 means it's on and working.
- So the thumb rule for conversion is use of 10 and 2. Our number system is on base 10 and computer is on base 2.

## 1.1. Decimal to Binary Conversion
- Keep dividing the number by 2 and the answer will be the reminders.
- Also there is a shortcut when we think like a switch on off.
	- $1 = 2^{0}$ On for 0th power = 1
	- $2 = 0*2^0 + 1*2^1 = 10$ Off for 0th power but on for 1st power 
	- $5 = 1*2^0 +0*2^1 + 1* 2^2 = 101$ 
- 0-th power will always be on for odd numbers.
 
### 1.1.1. Binary to Decimal



---

# 2. Bit Manipulation

- We know Binary conversions. `Bin2dec` and `dec2Bin`
## 2.1. Bitwise Operators
- When we apply a bitwise operator on two decimal numbers those numbers converts to *Binary Numbers and then the operations gets applied on those 0 and 1*
- Ex - 3 (0011) 5(0101) 9(1001)
### 2.1.1. And (&) Operator
- && means the logical and.
- *Rule* - 1 only when both are 1

|     | AND |     |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  0  |
|  1  |  0  |  0  |
|  1  |  1  |  1  |
- so for `3 & 5` 
```
3 = 0 0 1 1
5 = 0 1 0 1
-------------
and 0 0 0 1 = 1 (decimal ans)

verify in code

9 = 1001
5 = 0101
----------
ans= 0001 = 1
```

### 2.1.2. OR (|) - 
- *Rule* - 0 only when both are 0. Opposite of AND

|     | OR  |     |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  1  |
```
OR
5 = 0101
9 = 1001
----------
or= 1101 = 13
```

### 2.1.3. XOR (^)
- Exclusive OR
- *Rule* - 0 for Same bit and 1 for different bits

|     | XOR |     |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  0  |
```
XOR
5 = 0101
9 = 1001
xor= 1100 = 12
```

---
## 2.2. Binary NOT 
- `tilde ~`
- `~1 = 0` and `~0 = 1`
- For num = 6 (110) so `~6` will be 001 (1)??? - Try
	- This is not 1, it's -7
	- *The reason* being - Any number in memory doesn't get stored in exactly this form (110) in binary but for a system of 32 bits that number will have zeros in all the missing bits.
		- Therefore the *1's Complement* form of 6 becomes `11111001` (for a 8 bit system let say).
		- Now to from this form we calculate the *2's Complement form* to know the actual answer, where the left most num denotes the sign [1 for negative and 0 for positive] called the **Most Significant Bit (MSB)** and apply the not on the rest of bits.
		- 1 1 1 1 1 0 0 1 -> -(0000110 + 1) = -111 = -7
- For num = 0 `~0` will be `111111111` in 1's complement and then `-(0000000+1) = -000000001` in [[3.12 Two's Complement]] which is -1
- So for any positive number, the answer will generally be negative.

## 2.3. Binary **Shift** Operator
- **Left Shift (<<)** - Remember the sign as Left shift less than.
	- `7 << 2` This means move the binary positions of 7 to the left by two positions. 111 will become 111 00 which is 28.
	- *Formula* - `a << b = a * 2^b` 
		- 7<< 2 = 7 * 2^2 = 28
- **Right Shift (>>)** - Move to the right side you might drop the nums
	- `7 >> 2` = two 1's will get dropped and will become 00001 = 1
	- *Formula -* `a >> b = a // 2^b` 
		- 7 // 4 = 1


# 3. Use of Bit Manipulation - in Problems
- **Bit Masking -** The number we use to access a specific bit in the byte of data is called the BitMask. In problems our main task will be to think of BitMask.
- Example - OddEven using Bit
	- We know any odd number has 1 at the last bit.
	- So we can do something to access the last bit only.
	- We apply the `&` operator with 1, and operator gives 1 only with 1, else 0. So all the number will either become 0 for even and 1 for odd.
```
- return num & 1 : 1 for odd, 0 means even
```

## 3.1. Check Power of 2
[[3.10 Get Set Clear i-th Bit]]

## 3.2. Clear last i bits of a number
```Pseudo
num = 15 and i = 2
15 = 1111
clear 2 bits = 1100 = 12
```
- Need a bitmask which will become 0.
	- `0 & 0 = 1 & 0 = 0`
	- So we need apply `&` with the last i-th bit having 0, every other bit needs to be 1.
	- If we choose a num having all 1 in it's bin and apply `num << i` that will make the last i bits 0
	- **The number having all digits 1 in its binary is`-1`**
## 3.3. Count Set Bits
Number of 1's. - [LC]()
##### 3.3.0.0.1. Strategy
- Found the last Bit. (We have seen how can we access the last digit in the power of 2).
	- `num & 1` will give the last digit.
		- 0 means last bit is 0.
		- Any other num will mean the last bit is 1
- Keep adding to the `Count` if the bit is non zero.
- And now we will want our num to get `shifted` to right and the last digit gets updated.
- We need to keep doing this till the time we reach the num as 0.


---

# 4. Get Set Clear i-th Bit

Given a number let say 6 (110) and asked the 2nd bit. bit count runs from the end.
- We need to think of the bit mask and the operation we can perform to find the i-th bit
- Either 0 or 1.
- If we take the binary number where every bit is `0` except the i-th position, and perform the `&` operation. `0&1 = 0` and `1&1 = 1` so if the bit is `0` that will make the number 0 else return something more than 1
### 4.0.1. Set
- if i-th bit is 0 set it to 1.
	- Apply `OR`
Clear
- if the i-th bit is 1 set it to 0.
	- Apply `&` to `~(1<<i)`


## 4.1. Check for Power of 2

```
Power of 2's in binary
2  ->  10
4  ->  100
8  ->  1000
16 ->  10000
32 ->  100000
```
- So the power of 2 has only one bit on and else is off.
```
Binary form 2^n -1
1  -> 1
3  -> 11
7  -> 111
15 -> 1111
31 -> 11111
```
- ***So the $2^n -1$ has all 1's all bit on.***
- So there is perfect mismatch.
###### 4.1.0.0.0.1. SO what will be the `4 & 3`
```
  100 
& 011
-------
  000
```
- If a number `num` is a power of 2 and the and operation between `num & (num-1)` will always be 0.
[LC 231](https://leetcode.com/problems/power-of-two/description/)
- There is an edge case for `num = 0` it's not a power of 2 but `0 & -1`

**In General `n & n-1` removes the lowest 1 (set) bit the rightmost 1.**
- This helps to solve the *Hamming Weight* Problem, The count of 1 bit in a num.
- Logic
```pseudo
Iterate through the num till it become 0
while num:
	num = num & num-1
at each iteration rightmost 1 will be 0 and slowly the num will be 0.


n =  12 → 1100
n-1 = 11 → 1011
----------------
n & (n-1) = 1000 → 8

```
This is *Brian Kernighan's Algorithm*

#### 4.1.0.1. Why Does `n & (n - 1)` Remove the Rightmost Set Bit?

1. When you subtract 1 from `n`, you **flip the rightmost 1 to 0** and **flip all 0s after it to 1s**.
2. So `n` and `n-1` differ at the **rightmost set bit**, which becomes 0 in `n & (n - 1)`.
- Suppose `n = 10100`
```
Binary:      1 0 1 0 0   ← original n
             ↓
Subtract 1:  1 0 0 1 1   ← flips the rightmost 1 and all 0s after

AND:         1 0 0 0 0   ← rightmost set bit gone!

```
- Notice how the **rightmost 1 (second position from the right)** is gone!
#### 4.1.0.2. Algorithm Logic Step-by-Step

```python
while n:
  n = n & (n - 1)   # remove the rightmost set bit
  count += 1        # we just removed 1 set bit, so increase count
```

- No of Iteration = No of 1's = Hamming Weight
 - [LC 190 Reverse Bit](https://leetcode.com/problems/reverse-bits/description/)
 - [LC 191 Count of 1's Bit ](https://leetcode.com/problems/number-of-1-bits/description/)

# 5. One's Complement




# 6. Two's Complement

**Two’s complement** is a mathematical method and a binary encoding scheme used to represent both positive and negative integers in binary form. It is the most common way computers store signed integers.

## 6.1. Why Use Two’s Complement?

- **Simplicity:** Arithmetic operations (addition, subtraction) are easy and efficient.
    
- **Single Zero:** Only one representation for zero (unlike some other systems).
    
- **Easy Negation:** Negating a number is straightforward.

## 6.2. How Does Two’s Complement Work?

Let’s see how to represent a negative number (e.g., -5) in 8-bit binary:

1. **Write the positive number in binary:**  
    5 in 8 bits: `00000101`
    
2. **Invert all the bits (one’s complement):**  
    `11111010`
    
3. **Add 1 to the result:**  
    `11111010` + `1` = `11111011`

So, **-5** in 8-bit two’s complement is:  
`11111011`
## 6.3. Example Table (8 bits)

|Decimal|Binary (Two’s Complement)|
|---|---|
|5|00000101|
|-5|11111011|
|-1|11111111|
|0|00000000|

## 6.4. How to Find Two’s Complement

For any N-bit number:

1. **Write the number in binary.**
    
2. **Invert all bits** (change 0 to 1, and 1 to 0).
    
3. **Add 1** to the result.

```Python
def print_twos_complement(n, bits):
	print(format(n & (2**bits - 1), f'0{bits}b'))

  

print_twos_complement(-1, 8) # 8 bits: 11111111

print_twos_complement(-1, 16) # 16 bits: 1111111111111111
```

### 6.4.1. Explanation
```python

n = -1 bits = 8 print(format(n & (2**bits - 1), f'0{bits}b'))
```

### 6.4.2. Bit Masking: `n & (2**bits - 1)`

- `2**bits` calculates 2 to the power of the number of bits. For 8 bits, `2**8 = 256`.
- `2**bits - 1` gives you a mask where all bits are 1. For 8 bits: `256 - 1 = 255`, which in binary is `11111111`.
    
- `n & (2**bits - 1)`  
    This performs a bitwise AND between `n` and the mask.
    
    - For `n = -1`, in Python, negative numbers are stored with an infinite number of leading 1s (in two’s complement).
        
    - The mask (`11111111`) keeps only the lowest 8 bits of `n`.
        
    - So, `-1 & 0xFF` (where `0xFF` is 255 in hex) results in `11111111` (8 bits).

##### 6.4.2.0.1. Formatting: `format(..., f'0{bits}b')`

- `format(value, '08b')`
    
    - `'08b'` means:
        
        - `0` → pad with zeros
            
        - `8` → total width is 8 digits
            
        - `b` → binary format
            
- This ensures the output is always 8 bits wide, padded with zeros if needed.
##### 6.4.2.0.2. Summary Table

|Code Part|What it does|
|---|---|
|`n & (2**bits - 1)`|Gets the lowest `bits` bits of `n`|
|`format(..., f'0{bits}b')`|Formats as zero-padded binary string|
|`print(...)`|Prints the result|

**In short:**  
The code takes a negative number, keeps only the desired number of bits (emulating two’s complement), and prints it as a binary string.

Let me know if you want to see how it works for other numbers or bit widths!
## 6.5. Why is it Useful?

- **Arithmetic is the same:** Adding negative and positive numbers works without special rules.
    
- **Efficient hardware:** Circuits are simpler and faster.
    

## 6.6. Quick Facts

- The leftmost bit (most significant bit) indicates the sign:  
    `0` = positive, `1` = negative.
    
- The range for N bits:  
    `-(2^(N-1))` to `(2^(N-1) - 1)`  
    (e.g., for 8 bits: -128 to 127)
    

**In summary:**  
Two’s complement is a clever way for computers to handle negative numbers, making binary arithmetic simple and efficient!

Let me know if you want to see more examples or a visualization!

---

# 7. Fast Exponentiation
The program to find $X^n$ runs in O(n) time. But with Bits we can find in O$(\log {n})$ time.

- For $X^n$ we use the binary expression of n
- Remember, for any digit `n` there will be at max $(\log_2 {n} + 1)$ length of binary digits.
	- So to find `3^5` we need 3 iteration at max using bits.
- We will keep a var `ans = 1`
```Pseudo
5 = 101 -> (3^1 * 1) * (3^2 * 0) * (3^4* 1) = 3^5

x = 3, n = 5

ans = 1
1. bit == 1
	ans = ans*x = 3
	x = x * x = 9
2. bit == 0:
	x = x * x = 81
3. bit == 1
	ans = ans*x = 81*3 = 243

Total 3 steps to calculate 5th power.
```






### 7.0.1. Code Block

```

```


