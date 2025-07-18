- **Problem Link** : [1903. Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/)
- **Date** : July 18, 2025
- **Topic** : [[Strings]]
- **Difficulty** : #Easy #StriverSheet

---
### Summary Description: 
- Given a number in form of a string. We have to return the Odd number in the str.
 
## Strategy & Key Insights
 - Main Focus is on the last digit, if the last digit is odd, the whole number is odd.
 - So we traverse from the right to left, when we found a odd digit, that becomes the odd number from the starting point.
 - `num = "45278"`
## PseudoCode (Brute-Force)
```
for ch in num:
	if ch%2 == 1:
		return num[st = 0 : end = i+1]
if we don't find any odd digit then return ""
```



## PseudoCode (Optimal)
```

```
