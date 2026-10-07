class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        track = [[] for _ in range(len(nums) + 1)]

        for key, value in count.items():
            track[value].append(key)

        res = []
        
        j = len(nums)
        while k > 0 and j > 0:
            if track[j] != []:
                for num in track[j]:
                    res.append(num)
                    k -= 1
            j -= 1
        
        return res