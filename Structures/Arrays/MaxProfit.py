
#single transaction

def maxProfit(prices: list[int]) -> int:
    maxprofit = 0
    bestBuyPrice = prices[0]
    #buy at min sell at max
    n = len(prices)
    for i in range(1, n):
        if prices[i] > bestBuyPrice:
            maxprofit = max(maxprofit, (prices[i]) - bestBuyPrice)
        bestBuyPrice = min(prices[i], bestBuyPrice)
    return maxprofit

print(maxProfit(prices= [100, 180, 260, 310, 40, 535, 695]))