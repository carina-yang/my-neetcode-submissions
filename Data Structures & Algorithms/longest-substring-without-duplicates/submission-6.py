class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        left = 0 
        characters = set() 
        max_length = 1
        characters.add(s[left])

        for i in range(1, len(s)): 
            while s[i] in characters: 
                characters.remove(s[left])
                left += 1
            
            max_length = max(i - left + 1, max_length)
            characters.add(s[i])
        
        return max_length
            
