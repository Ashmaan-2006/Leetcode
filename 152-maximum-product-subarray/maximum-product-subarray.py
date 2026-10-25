class Solution(object):
    def maxProduct(self, nums):

        maximum = nums[0]
        minimum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            maxNum = max(num, num * maximum, num * minimum)
            minNum = min(num, num * minimum, num * maximum)

            maximum = maxNum
            minimum = minNum

            result = max(result, maxNum)

        return result