
'''
    Problem: https://leetcode.com/problems/fruits-into-baskets-ii/description/
'''

## Brute Solution
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        placed = 0
        used_basket = set()
        n = len(fruits)
        for quantity in fruits:
            for j in range(n):
                if baskets[j] >= quantity and j not in used_basket:
                    placed += 1
                    used_basket.add(j)
                    break
        return n - placed




