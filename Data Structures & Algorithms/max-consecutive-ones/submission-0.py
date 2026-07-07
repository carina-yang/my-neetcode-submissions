class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0

        for idx, num in enumerate(nums):
            if num == 1:
                res = max(res, idx - l + 1)
            if num == 0:
                l = idx + 1

        return res