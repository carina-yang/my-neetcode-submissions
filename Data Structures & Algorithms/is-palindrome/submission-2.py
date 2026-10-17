class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:

            r_isalnum = s[r].isalnum()
            l_isalnum = s[l].isalnum()

            if not r_isalnum:
                r -= 1
            elif not l_isalnum:
                l += 1
            elif r_isalnum and l_isalnum and s[r] != s[l]:
                return False
            else:
                r -= 1
                l += 1
        
        return True