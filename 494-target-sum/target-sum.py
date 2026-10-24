class Solution(object):
    def findTargetSumWays(self, nums, target):

        dp = {}

        currsum = 0

        def backtrack(i, currsum):

            if i == len(nums):
                if currsum == target:
                    return 1
                else:
                    return 0
                
            if (i, currsum) in dp:
                return dp[(i, currsum)]

                
            dp[(i, currsum)] = (backtrack(i + 1, currsum - nums[i]) + backtrack(i + 1, currsum + nums[i]))

            return dp[(i, currsum)]

            
        return backtrack(0,0)