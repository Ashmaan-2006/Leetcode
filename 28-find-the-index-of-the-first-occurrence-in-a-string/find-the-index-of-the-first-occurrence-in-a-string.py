class Solution(object):
    def strStr(self, haystack, needle):

        # Edge case: If needle is empty, the index is 0
        if not needle:
            return 0
        
        n_len = len(needle)
        h_len = len(haystack)

        for i in range(h_len - n_len + 1):
            # Check if the slice matches the needle
            if haystack[i : i + n_len] == needle:
                return i
        
        # If no match is found after the loop
        return -1