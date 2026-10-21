class Solution(object):
    def minSubArrayLen(self, target, nums):

        pointer1 = 0
        min_length = float('inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:

                if total - nums[pointer1] < target:
                    break

                total -= nums[pointer1]
                pointer1 += 1

            if total >= target:
                length = i - pointer1 + 1
                min_length = min(length, min_length)

        if min_length == float('inf'):
            return 0

        return min_length