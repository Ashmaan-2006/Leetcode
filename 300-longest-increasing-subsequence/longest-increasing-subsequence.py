class Solution(object):
    def lengthOfLIS(self, nums):

        n = len(nums)
        dp = {}

        for i in range(n):
            dp[i] = 1


        for i in range(n):
            for j in range(i):

                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)


        return max(dp.values())
        