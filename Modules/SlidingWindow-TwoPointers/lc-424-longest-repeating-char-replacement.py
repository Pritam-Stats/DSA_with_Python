'''
Problem: https://leetcode.com/problems/longest-repeating-character-replacement/
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = 0
        maxLen = 0
        n = len(s)
        left, right = 0, 0

        while right < n:
            freq[s[right]] = freq.get(s[right], 0) + 1

            maxF = max(maxF, freq[s[right]])

            while (right - left + 1) - maxF > k:
                freq[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
