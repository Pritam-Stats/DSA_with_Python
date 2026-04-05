'''  
Problem: Buy and Sell Stocks
Link/Platform: LC 121
Technique: 
Core Idea & Intuition: keep track of the minPrice to buy and maxPrice to sell and keep updating
Invariant: 
Common Mistake: 
Time: O(n)
Space: O(1)
''' 
#single transaction

def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    bestBuyPrice = prices[0]
    #buy at min sell at max
    n = len(prices)
    for i in range(1, n):
        if prices[i] > bestBuyPrice:
            maxProfit = max(maxProfit, (prices[i]) - bestBuyPrice)
        bestBuyPrice = min(prices[i], bestBuyPrice)
    return maxProfit

print(maxProfit(prices= [100, 180, 260, 310, 40, 535, 695]))    #buy at 40 sell 695 = 655
