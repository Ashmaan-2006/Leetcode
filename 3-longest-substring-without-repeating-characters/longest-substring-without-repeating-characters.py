class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Maps character -> its last seen index
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If we've seen this char and it's inside our current window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move left pointer to the right 
                left = char_index_map[current_char] + 1
            
            # Update the character's last seen position
            char_index_map[current_char] = right
            
            # Calculate window size: (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length