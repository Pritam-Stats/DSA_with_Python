def lps1(s: str)-> int:
    n = len(s)
    dp = [[0] *(n+1) for _ in range(n+1)]
    rev = s[::-1]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]

def lps2(s: str)-> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]


if __name__ == "__main__":
    print('First Approach')
    print(lps1("bbbab") == 4)
    print(lps1("cbbd") == 2)
    print('\nUsing the second Approach:')
    print(lps2("bbbab") == 4)
    print(lps2("cbbd") == 2)