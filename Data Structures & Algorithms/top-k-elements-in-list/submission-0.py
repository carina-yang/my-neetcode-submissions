class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        for num in nums:
            if num in track:
                track[num] += 1
            else:
                track[num] = 1
        res = list(track.items())
        res.sort(reverse=True, key=lambda x: x[1])
        res = [x[0] for x in res]
        return res[:k]