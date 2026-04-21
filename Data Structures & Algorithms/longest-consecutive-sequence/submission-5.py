class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))

        if len(sorted_nums) == 0:
            return 0

        longest = 1
        temp_len = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == (sorted_nums[i - 1] + 1):
                temp_len += 1
                longest = max(temp_len, longest)
            else:
                temp_len = 1
        
        return longest

            