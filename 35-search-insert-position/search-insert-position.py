class Solution(object):
    def searchInsert(self, nums, target):

        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate middle index 
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If not found, 'left' is the insertion point
        return left