class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        window = {}

        required = len(need)
        formed = 0

        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]

            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]

