class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lowest = prices[0]
        diff = 0

        for i in range(len(prices)):

            if len(prices) > (i + 1):

                diff = max((prices[i + 1] - lowest), diff)

                lowest = min(lowest, prices[i + 1])

        return diff

        