class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = []
        postfix_prods = [0] * len(nums)
        pre_prod = 1
        post_prod = 1
        for i in range(len(nums)):
            pre_prod *= nums[i]
            prefix_prods.append(pre_prod)
            post_prod *= nums[len(nums) - 1 - i]
            postfix_prods[len(nums) - 1 - i] = post_prod
        
        output = []
        for i in range(len(nums)):
            prod_except_self = 1
            if (i - 1) >= 0:
                prod_except_self *= prefix_prods[i - 1]
            if (i + 1) < len(nums):
                prod_except_self *= postfix_prods[i + 1]
            output.append(prod_except_self)
        
        return output