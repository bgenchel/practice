"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def posDiffProfit(self, prices):
        total_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        return total_profit

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        if len(prices) <= k/2:
            return self.posDiffProfit(prices)

        buys = [float('-inf')]*(k + 1)
        sells = [0]*(k + 1)
        for price in prices:
            for i in xrange(1, k+1):
                buys[i] = max(buys[i], sells[i - 1] - price)
                sells[i] = max(sells[i], buys[i] + price)
        return sells[k]

