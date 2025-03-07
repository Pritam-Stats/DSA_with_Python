# n-th fibonacci term
def fib(n: int) -> int:
    f0, f1 = 0, 1
    if n <= 1:
        return n
    
    for i in range(2, n+1):
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn
#TC = O(n)  #most optimized
# print(fib(6))

# ------------------------------------------------------------

## FIBONACCI SEQUENCE - RECURSION

def fibonacci(n: int):
    if n <= 1:      #base case 
        return n
    
    return fibonacci(n - 2) + fibonacci(n - 1)
    

# for i in range(10):
#     print(fibonacci(i), end= " ")

# TC = O(2^n)


####################
# DP

# approach 1 : Recursive + Memorization
# Memoization is a technique where we cache previously computed values so that we don’t compute them again.

from functools import lru_cache

@lru_cache      #Built in memory
def fibo_memory(n):
    if n <= 1:
        return n
    return fibo_memory(n - 1) + fibo_memory(n - 2)

# print(fibo_memory(4))

# We store computed Fibonacci values using @lru_cache, so we never recalculate them.
# This reduces the time complexity from O(2^n) to O(n)

## Tabulation storing in arrays list

def fibo_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)  #an empty to store or update

    dp[0], dp[1] = 0, 1 #to calculate the rest

    for i in range(2, n+1):
        dp[i] = dp[i -1] + dp[i - 2]
    return dp[:]    #returns all | dp[n] will the the n'th term

print(fibo_dp(4))