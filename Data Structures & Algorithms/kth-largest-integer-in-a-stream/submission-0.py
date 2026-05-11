import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.small = []
        self.large = []
        self.k = k

        for num in nums:
            self._insert(num)
        print("done")

    def _insert(self, val: int) -> None:
        heapq.heappush(self.small, -1 * val)

        if self.small and self.large and (self.small[0] * -1) > self.large[0]:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        
        if (len(self.small) + len(self.large)) >= self.k:
            while len(self.large) < self.k:
                tmp = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, tmp) 
            while len(self.large) > self.k:
                tmp = heapq.heappop(self.large)
                heapq.heappush(self.small, -1 * tmp) 
        print(self.small)
        print(self.large)
        
    def add(self, val: int) -> int:
        self._insert(val)
        return self.large[0]
        

