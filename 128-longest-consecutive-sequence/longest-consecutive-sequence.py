class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        result = 0

        while nums_set:
            num = nums_set.pop()
            count = 1

            left = num - 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1
                count += 1

            right = num + 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1
                count += 1

            result = max(result, count)

        return result