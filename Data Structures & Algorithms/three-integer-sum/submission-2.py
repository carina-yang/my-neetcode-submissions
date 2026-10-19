class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        nums.sort()

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, N - 1

            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue

                if r < N - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue

                val = nums[i] + nums[l] + nums[r]
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res
