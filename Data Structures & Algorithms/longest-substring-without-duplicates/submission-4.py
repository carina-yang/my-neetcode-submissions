class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        substring = set()
        max_length = 0

        for R in range(len(s)):
            max_length = max(max_length, len(substring))
            while s[R] in substring:
                substring.remove(s[L])
                L += 1
            substring.add(s[R])
            
        return max(max_length, len(substring))
        

