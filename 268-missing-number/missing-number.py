class Solution(object):
    def missingNumber(self, nums):

        numbers = set(nums)

        for i in range(len(nums) + 1):
            if i not in numbers:
                return i

        