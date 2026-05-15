import heapq

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -1 * num)
        if self.low and self.high and -1 * self.low[0] > self.high[0]:
            heapq.heappush(self.high, -1 * heapq.heappop(self.low))
        
        if self.low and len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -1 * heapq.heappop(self.low))
        elif self.high and len(self.high) > len(self.low) + 1:
            heapq.heappush(self.low, -1 * heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -1 * self.low[0]
        elif len(self.low) < len(self.high):
            return self.high[0]
        else:
            return ((-1 * self.low[0]) + self.high[0]) / 2
        
        