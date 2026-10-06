class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        res = []

        for key, value in count.items():
            if k == 0:
                break
            res.append(key)
            k -= 1
        
        return res