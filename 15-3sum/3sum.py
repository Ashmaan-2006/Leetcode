class Solution(object):
    def threeSum(self, nums):

        nums.sort()

        triplets = []

        for index, value in enumerate(nums):

            if (value == nums[index - 1]) and (index > 0):
                continue



            #start at the end, as this way we will have a very clear way to indicate to move left or right since the numbers are sorted
            right = len(nums) - 1

            left = index + 1


            while (right > left):

                current_sum = value + nums[left] + nums[right]

                if (current_sum > 0) and (right > left):

                    right -= 1

                    while nums[right] == nums[right + 1] and (right > left):
                        right -= 1

                elif (current_sum < 0) and (right > left):

                    left += 1

                    while (nums[left] == nums[left - 1]) and (right > left):
                        left += 1

                else: 

                    triplets.append([value, nums[left], nums[right]])

                    if (right > left):

                        left += 1
                    
                    else:
                        continue

                    while nums[left] == nums[left - 1] and (right > left):
                        left += 1

        return triplets







        