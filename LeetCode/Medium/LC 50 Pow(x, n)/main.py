class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        while n:
            if n&1 != 0:
                ans *= x
                x *= x
            else:
                # 0  bit
                x *= x
            n = n>> 1
        return ans

sol = Solution()
print(sol.myPow(x = 2.00000, n = 10) == 1024.00000)
print(sol.myPow(x = 2.10000, n = 3).__round__(5) == 9.26100)
print(sol.myPow(x = 2.00000, n = -2) == 0.25000)