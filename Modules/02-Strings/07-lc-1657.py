'''  
    Author: Pritam
'''
'''  
Problem: 
Technique: 
Intuition: 
Mistake: 
Time: 
Space: 
'''


from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths differ, they cannot be close
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        # 1) Same set of characters
        if set(c1.keys()) != set(c2.keys()):
            return False

        # 2) Same multiset of frequencies
        return sorted(c1.values()) == sorted(c2.values())
sol = Solution()
sol.closeStrings("abc", "bca")

sol.closeStrings("abbzzca", "babzzcz")
