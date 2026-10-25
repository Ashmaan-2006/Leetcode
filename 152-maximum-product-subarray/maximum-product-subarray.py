class Solution(object):
    def maxProduct(self, nums):

        maximum = nums[0]
        maxNum = nums[0]
        minNum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            maxNum = max(num, num * maxNum, num * minNum)
            minNum = min(num, num * minNum, num * maximum)

            maximum = maxNum

            result = max(result, maxNum)

        return result