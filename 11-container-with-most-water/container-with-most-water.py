class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        max_container = 0

        while right > left:

            container = min(height[left], height[right]) * (right - left)

            max_container = max(max_container, container)

            if height[right] > height[left]:
                left += 1

            else:
                right -= 1


        return max_container


                
                



        
        