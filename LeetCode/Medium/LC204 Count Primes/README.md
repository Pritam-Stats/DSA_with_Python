- **Problem Link** : [204. Count Primes](https://leetcode.com/problems/count-primes/)
- **Date** : July 19, 2025
- **Topic** : [[1.00 Maths & Combinatorics - Number Theory]]
- **Difficulty** : #Medium 

---
### Summary Description: 
- Given a number `n` count all the prime strictly less than `n`.
	- Not including n

## PseudoCode (Brute-Force)
```
Run through all number and check
```

## Optimal Approach

Prime Number Algorithms and Sieve Techniques
A prime number is a natural number greater than 1 that has exactly two distinct positive divisors — 1 and itself.

***Basic Primality Check:*** To check if a number n is prime, try dividing it by numbers from 2 to n. If any number divides it, then n is not prime; otherwise, it is.

***Optimized Method (Square Root Check):*** We only need to check up to √n because if n has a factor larger than √n, the corresponding smaller factor must be less than √n.

So if no number from 2 to √n divides n, then n is prime.
```Python
import math

def isPrime(n):
    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
  n = 7
  if(isPrime(n)): 
    print("true")
  else:
    print("false")
```

## Best method to find the Primes
***Sieve of Eratosthenes:*** The Sieve of Eratosthenes is an efficient algorithm to find all prime numbers up to a given number n.

***Note:*** It is much faster than checking each number individually using the basic method.
```Python
def sieve(n):
   
    #Create a boolean list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2

    # Sieve of Eratosthenes algorithm
    while p * p <= n:
        if prime[p]:
            
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res

if __name__ == "__main__":
    n = 35
    res = sieve(n)
    for ele in res:
        print(ele, end=' ')
```

#### Key Strategy
Pick a prime, mark all it's multiple non prime, every multiple will be at p step.
- Prints all the primes less than equal to n.