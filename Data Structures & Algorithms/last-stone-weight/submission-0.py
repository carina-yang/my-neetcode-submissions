import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-x for x in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            x = heapq.heappop(arr) * -1 
            y = heapq.heappop(arr) * - 1
            if x != y:
                heapq.heappush(arr, -1 * (x - y))
        
        if len(arr) == 1:
            return arr[0] * -1
        else:
            return 0
