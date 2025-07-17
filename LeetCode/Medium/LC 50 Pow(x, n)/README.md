## LeetCode 50 Power (x, n)
- Problem Link: [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
- **Date :** July 17, 2025 | 7:27 PM
- **Topic** : [[3.02 Bit Manipulation]] [[3.13 Fast Exponentiation]]
- **Difficulty** : #Medium 

---
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



