class Solution(object):
    def twoSum(self, nums, target):
        for number in range(len(nums)):
            for number2 in range(number + 1, len(nums)):
                if nums[number] + nums[number2] == target:
                    return [number, number2]
