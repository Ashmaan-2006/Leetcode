class Solution(object):
    def findTargetSumWays(self, nums, target):

        dp = {}

        def backtrack(i, curr_sum):

            if i == len(nums):
                if curr_sum == target:
                    return 1

                else:
                    return 0

            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = (backtrack(i + 1, curr_sum + nums[i]) + (backtrack(i + 1, curr_sum - nums[i])))

            return dp[(i, curr_sum)]
        
        return backtrack(0,0)