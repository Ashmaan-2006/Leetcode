class Solution(object):
    def searchRange(self, nums, target):
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            bound = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        # Look for earlier occurrences to the left
                        high = mid - 1
                    else:
                        # Look for later occurrences to the right
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound

        start = findBound(isFirst=True)
        # If the start isn't found, the target isn't in the array
        if start == -1:
            return [-1, -1]
        
        end = findBound(isFirst=False)
        
        return [start, end]