class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in track:
                return [track[diff], i]

            track[nums[i]] = i