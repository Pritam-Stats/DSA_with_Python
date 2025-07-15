class Solution:
    def countPalindromicSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand_around_center(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1

        for i in range(n):
            expand_around_center(i, i)     # odd-length palindromes
            expand_around_center(i, i + 1) # even-length palindromes

        return count

ans = Solution()
print(ans.countPalindromicSubstrings("abba") == 2)
print(ans.countPalindromicSubstrings("aaa") == 3)