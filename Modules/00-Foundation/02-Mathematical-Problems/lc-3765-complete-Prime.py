'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/complete-prime-number/description/
Technique: brute
Intuition: check isPrime for each digit
Mistake: Maybe not optimal and 2 is a Prime
Time: O(d * sq(n))
Space: (1₹)
''' 
class Solution:
    def completePrime(self, num: int) -> bool:
        '''
            Author: Pritam
        '''
        from functools import lru_cache

        @lru_cache(None)
        def isPrime(n):
            if n <= 1:
                return False
            for d in range(2, int(n**0.5) + 1):
                if n % d == 0:
                    return False
            return True

        digit = len(str(num))
        if digit == 1:
            return isPrime(num)

        if not isPrime(num):
            return False

        for p in range(1, digit):
            if not isPrime(num//(10**p)):
                return False

            if not isPrime(num % (10**p)):
                return False

        return True
