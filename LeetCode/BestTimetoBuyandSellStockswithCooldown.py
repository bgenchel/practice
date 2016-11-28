"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again). After you sell your stock, you cannot buy
stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        prev_buy = 0 # this value doesn't matter, will be overwritten.
        buy = -prices[0]
        prev_sell = 0
        sell = 0
        prev_rest = 0
        rest = 0
        for price in prices:
            prev_buy = buy
            buy = max(rest - price, prev_buy)

            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)

            prev_rest = rest
            rest = max(prev_sell, prev_rest)

            print "\nCURR PRICE = %d"%price
            print "prev_buy: %d"%prev_buy
            print "buy: %d"%buy
            print "prev_sell: %d"%prev_sell
            print "sell: %d"%sell
            print "prev_rest: %d"%prev_rest
            print "rest: %d"%rest

        return max(rest, sell)


class SolutionTwo(object):
    """
    from: https://discuss.leetcode.com/topic/30421/share-my-thinking-process/2,
    uses a clever dp that my solution seems to incorrectly immitate. Here 
    for testing.
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
            print "\nCURR PRICE = %d"%price
            print "prev_buy: %d"%prev_buy
            print "buy: %d"%buy
            print "prev_sell: %d"%prev_sell
            print "sell: %d"%sell
        return sell

if __name__ == '__main__':
    prices = map(int, raw_input("enter prices:  ").split())
    s = Solution()
    # s = SolutionTwo()
    print s.maxProfit(prices)


