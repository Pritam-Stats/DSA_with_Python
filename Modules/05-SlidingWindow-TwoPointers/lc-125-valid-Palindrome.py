'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/valid-palindrome/description/
Technique: Two Pointer
Intuition: start from both end - skip the invalid chars which is non-alphanums
Mistake: Earlier i was brute forcing, using reverse extra space
Time: O(n) -> theoretically n/2
Space: O(1)
''' 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1

        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True