class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        lower_s = s.lower()
        
        while L < R:
            L_char = lower_s[L]
            R_char = lower_s[R]

            if L_char.isalnum() and R_char.isalnum():
                if L_char != R_char:
                    return False
                L += 1
                R -= 1
            elif not L_char.isalnum():
                L += 1
            elif not R_char.isalnum():
                R -= 1
        
        return True