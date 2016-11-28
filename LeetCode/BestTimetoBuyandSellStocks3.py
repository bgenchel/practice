"""
Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete at most
two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class SolutionOne(object):
    """
    My solution, runs through array forward and backwards to find
    two max profit diffs, then sums them. O(n)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        forward_profits = [-1]*len(prices)
        backward_profits = [-1]*len(prices)

        min_price = prices[0]
        max_price = prices[0]
        max_profit = 0
        i = 0
        while i < len(prices):
            curr = prices[i]
            if curr < min_price:
                min_price = curr
                max_price = curr
            elif curr > max_price:
                max_price = curr
                if max_price - min_price > max_profit:
                    max_profit = max_price - min_price
            forward_profits[i] = max_profit
            i += 1

        min_price = prices[-1]
        max_price = prices[-1]
        max_profit = 0
        i = len(prices) - 1
        while i >= 0:
            curr = prices[i]
            if curr < min_price:
                min_price = curr
                if max_price - min_price > max_profit:
                    max_profit = max_price - min_price
            elif curr > max_price:
                max_price = curr
                min_price = curr
            backward_profits[i] = max_profit
            i -= 1

        total_profit = 0
        for i in xrange(len(forward_profits)):
            total_profit = max(total_profit, forward_profits[i] + backward_profits[i])

        # print "prices: {}".format(prices)
        # print "forward_profit: {}".format(forward_profits)
        # print "backward_profits: {}".format(backward_profits)
        return total_profit


class SolutionTwo(object):
    """
    cdai's solution: https://discuss.leetcode.com/topic/60343/very-understandable-solution-by-reusing-problem-iii-idea
    uses 4 variables to keep track of two buy and sell pairs. Scans through the
    array only one time. Allegedly DP. O(n)
    """
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for price in prices:
            # buy1 is the profit after the first buy, it will be negative since
            # you haven't sold anything. the largest negative is the smallest
            # positive
            buy1 = max(buy1, -price)
            # sell one is the profit after the first sell; since buy 1 is
            # negative, this represents a difference between prices. We add
            # the price because we're selling at that price.
            sell1 = max(sell1, buy1 + price)
            # buy two is the profit after the second buy; since you're buying
            # stocks, your total profit is decreasing. The largest total profit
            # will subtract the smallest price.
            buy2 = max(buy2, sell1 - price)
            # sell two is the profit after the second sell, our final answer.
            # since we're selling back, we add the price to our profit.
            sell2 = max(sell2, buy2 + price)

            print "buy1: %d, sell1: %d, buy2: %d, sell2: %d"%(buy1, sell1, buy2, sell2)

        return sell2

if __name__ == '__main__':
    prices = map(int, raw_input().split())
    sol = SolutionTwo()
    print sol.maxProfit(prices)

