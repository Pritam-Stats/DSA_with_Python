class Solution:
    def countPalindromeSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand_around_center(left: int, right: int) -> None:
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand_around_center(i, i)  #for odd len palindromes
            expand_around_center(i, i+1)    #for even 

        return count

    def countPalindromeSubStrings_DP(self, s: str) -> int:
        n = len(s)
        dp = [[]]
        count = 0



        return count



sol = Solution()
print(sol.countPalindromeSubstrings("aba") == 4)
print(sol.countPalindromeSubstrings("abc") == 3)
print(sol.countPalindromeSubstrings("aaa") == 6)
print("\n###### Using DP Table ######")
print(sol.countPalindromeSubStrings_DP("aba") == 4)
print(sol.countPalindromeSubstrings_DP("abc") == 3)
print(sol.countPalindromeSubstrings_DP("aaa") == 6)