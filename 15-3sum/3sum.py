class Solution(object):
    def threeSum(self, nums):
        result = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):

                num1 = nums[i]
                num2 = nums[j]

                third = -(num2 + num1)

                if third in seen:
                    result.add(tuple(sorted([num1, num2, third])))

                seen.add(num2)
                    
        return [list(triplet) for triplet in result]
                    


        