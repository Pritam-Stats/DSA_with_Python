'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/richest-customer-wealth/
Technique: max row sum
Intuition: Basic - travel and update max
Mistake: 
Time: O(n)
Space: 1
''' 


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # basically return max rowsum
        maxRowSum = 0
        n = len(accounts)
        m = len(accounts[0])

        for i in range(n):
            maxRowSum = max(maxRowSum, sum(accounts[i]))

        return maxRowSum
