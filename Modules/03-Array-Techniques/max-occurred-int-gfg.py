

'''
    Problem: https://practice.geeksforgeeks.org/contest/code-catalyst/problems
'''

class Solution:
    def maxOccured(self, L, R):
        #code here
        freq = {}

        for l, r in zip(L,R):
            freq[l] = freq.get(l, 0) + 1
            freq[r+1] = freq.get(r+1, 0) -1


        maxF = 0
        ans = 0
        curr = 0
        for x in sorted(freq):
            curr += freq[x]

            if curr > maxF:
                maxF = curr
                ans = x
        return ans




s = Solution()
s.maxOccured([1,5,9,13,21], [15,8,12,20,30])    #5

s.maxOccured([1,4,3,1], [15, 8, 5,4])   #4

