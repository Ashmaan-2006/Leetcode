class Solution(object):
    def canPartition(self, nums):

        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = {}

        def backtrack(i, currsum):

            if currsum == target:
                return True

            if i == len(nums) - 1:
                return False

            if (i, currsum) in dp:
                return dp[(i, currsum)]

            dp[i, currsum] = backtrack(i + 1, currsum + nums[i]) or backtrack(i + 1, currsum)

            return (backtrack(i + 1, currsum + nums[i]) or backtrack(i + 1, currsum))

        return backtrack(0, 0)


            
