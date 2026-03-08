class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        
        for i in range (len(nums)):
            
            count[nums[i]] = count.get(nums[i], 0) + 1


            if count.get(nums[i]) > 1:
                return True

        return False

