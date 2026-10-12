class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        largest = 0

        for index in range(1, len(arr) - 1):

            left = index - 1
            right = index + 1

            if (arr[left] < arr[index]) and (arr[right] < arr[index]):
                count = 1
            
            else:
                continue

            while (left >= 0) and (arr[left] < arr[left + 1]):
                count += 1
                left -= 1

            while (right <= len(arr) - 1) and (arr[right] < arr[right - 1]):
                count += 1
                right += 1

            largest = max(largest, count)

        return largest


