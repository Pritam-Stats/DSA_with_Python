def maxProfit(prices : list) -> int:
    maxprofit = 0
    n = len(prices)

    for i in range(1, n):
        if prices[i] > prices[i-1]:
            maxprofit += prices[i] - prices[i -1]

    return maxprofit

print(maxProfit(prices=[100, 180, 260, 310, 40, 535, 695])) #865