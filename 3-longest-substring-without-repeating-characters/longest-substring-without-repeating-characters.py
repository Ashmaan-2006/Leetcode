class Solution(object):
    def lengthOfLongestSubstring(self, s):

        last = {}   # char -> last index we saw it at
        left = 0
        best = 0

        for right, ch in enumerate(s):
        # if we've seen ch AND it's inside the current window, move left
        
            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            last[ch] = right
            best = max(best, right - left + 1)

        return best