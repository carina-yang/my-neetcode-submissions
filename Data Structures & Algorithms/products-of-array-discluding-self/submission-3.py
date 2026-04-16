class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = 1
        postfix = 1
        for i in range(n):
            output[i] *= prefix
            output[n - 1 - i] *= postfix
            prefix *= nums[i]
            postfix *= nums[n - 1 - i]
        
        return output