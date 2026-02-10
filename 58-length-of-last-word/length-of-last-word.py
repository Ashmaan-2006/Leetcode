class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()

        if not words:
            return 0
            
        # Return the length of the last element in the list
        return len(words[-1])