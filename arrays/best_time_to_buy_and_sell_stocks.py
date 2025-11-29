# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    profit = 0
    
    for sell in range(1, len(prices)):
        if prices[buy] < prices[sell]:
            profit += prices[sell] - prices[buy]
            
        buy += 1
        sell += 1
    
    return profit
