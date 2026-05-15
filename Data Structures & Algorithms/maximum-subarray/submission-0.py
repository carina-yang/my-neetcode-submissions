class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = float("-inf")

        for n in nums:
            currSum = max(currSum, 0) + n
            maxSum = max(currSum, maxSum)
        
        return maxSum