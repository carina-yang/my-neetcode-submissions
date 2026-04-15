class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        for num in nums:
            if num in track:
                track[num] += 1
            else:
                track[num] = 1
        
        # bucket = [[]] * (len(nums) + 1)
        # ^^^ Does not work
        bucket = [[] for _ in range(len(nums) + 1)]

        for key in track:
            bucket[track[key]].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            res += bucket[i]
            if len(res) == k:
                return res