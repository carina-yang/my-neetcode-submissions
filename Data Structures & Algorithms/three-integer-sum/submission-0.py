class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()

        for i in range(n - 2):

            left = i + 1
            right = n - 1
            
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return list(res)
                    