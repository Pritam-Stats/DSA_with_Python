'''Longest Common Subsequence
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/dynamic-programming-gfg-160/problem/longest-common-subsequence-1587115620
Given two strings s1 and s2, return the length of their longest 
common subsequence (LCS). If there is no common subsequence, r
return 0.

'''
def lcs(s1:str, s2: str) -> int:
    """TC = O(n * m)
    """
    #we will maintain a matrix to keep track of the len
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]  #mat of m+1 rows and n+1 cols
    #ans will be dp[m][n]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 #see the diagonal
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m][n]

if __name__ == "__main__":
    print("Correct Answer will return TRUE.")
    print(lcs("ABCDGH", s2 = "AEDFHR") == 3)    #adh
    print(lcs(s1 = "ABC", s2 = "AC") == 2)
    print(lcs(s1 = "XYZW", s2 = "XYWZ") == 3)   #xyz or xyw
    print(lcs(s1= "ABCDEF", s2 = "ACFEDC") == 3)    #acd