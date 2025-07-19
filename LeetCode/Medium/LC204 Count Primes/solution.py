class Solution:
    def countPrimes(self, n: int) -> int:
        #seive 
        if n <2:
            return 0

        isPrime = [True] * n    #there will two extra true 0 and 1
        p = 2

        while p*p <= n:
            if isPrime[p]:
                for i in range(p*p, n, p):
                    isPrime[i] = False

            p += 1
        
        return sum(isPrime)-2

# asked for strictly less than n

sol = Solution()
print(sol.countPrimes(0) == 0)
print(sol.countPrimes(1) == 0)
print(sol.countPrimes(2) == 0)
print(sol.countPrimes(10) == 4)
print(sol.countPrimes(1000))
