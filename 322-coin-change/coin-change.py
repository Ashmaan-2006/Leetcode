class Solution(object):
    def coinChange(self, coins, amount):


        # As it goes down by 1, when indexing... need complete amount
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        
        for i in range(1, amount + 1):

            for c in coins:

                if i >= c:

                    dp[i] = min(dp[i], 1 + dp[i - c])

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]
        