class Solution(object):
    def sumOfSquares(self, nums):
        
        total = 0

        for i in range(0, len(nums)):

            if len(nums) % (i + 1) == 0:

                total += nums[i] * nums[i]

        return total



            # loop through to find special elements

            # takes those elements and square them, and then sum that


        