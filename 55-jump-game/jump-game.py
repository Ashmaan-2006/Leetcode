class Solution(object):
    def canJump(self, nums):

        last_index = len(nums) - 1

        count = 0

        for i in range(len(nums)):

            if count >= last_index:
                return True
            

            if count < i:
                return False


            count = max(count, nums[i] + i)

        return True


        