'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
Technique: contribution and prefix sum
Intuition: calculate contribution - valid words are those which starts and ends with a vowel -> calculate ps of the contribution -> then append the ans according to the queries
Mistake: prefix sum calculation and return procedure confusion
Time: 
Space: 
'''

class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)
        contri = []
        for w in words:
            if w[0] in vowel and w[-1] in vowel:
                contri.append(1)
            else:
                contri.append(0)
        # print(contri)

        #prefix sum on contri
        ps = [0]*n
        currSum = 0
        for i in range(n):
            currSum += contri[i]
            ps[i] = currSum
        # print(ps)

        ans = []
        for q in queries:
            l, r = q
            if l == 0:
                # print(ps[r])
                ans.append(ps[r])
            else:
                # print(ps[r] - ps[l-1])
                ans.append(ps[r] - ps[l-1])
        return ans

    
s = Solution()
print(s.vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
# s.vowelStrings(["a","e","i"], [[0,2],[1,4],[1,1]])

        
        