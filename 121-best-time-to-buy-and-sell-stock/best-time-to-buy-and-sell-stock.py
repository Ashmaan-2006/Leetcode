class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        diff = 0

        for price in prices[1:]:
            diff = max(diff, price - min_price)
            min_price = min(min_price, price)

        return diff
                

        