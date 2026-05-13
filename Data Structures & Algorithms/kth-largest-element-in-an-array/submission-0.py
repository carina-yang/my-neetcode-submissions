import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [_ * -1 for _ in nums]
        heapq.heapify(new_nums)

        res = None
        for i in range(k):
            res = -1 * heapq.heappop(new_nums)
        
        return res