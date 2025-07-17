class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci style recurrsion
        if n ==0 or n==1:
            return 1

        dp = [0] * (n+1)    # 0 to n
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        
sol = Solution()

if __name__ == "__main__":
    print(sol.climbStairs(2) == 2)
    print(sol.climbStairs(3) == 3)