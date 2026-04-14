class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2)
        for idx, ele in enumerate(nums):
            ans[idx] = ele
            ans[idx + n] = ele
        return ans

