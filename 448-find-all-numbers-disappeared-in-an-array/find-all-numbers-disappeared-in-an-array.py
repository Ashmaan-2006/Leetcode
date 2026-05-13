class Solution(object):
    def findDisappearedNumbers(self, nums):

        seen = set(nums)
        non_appear = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                non_appear.append(i)

        return non_appear