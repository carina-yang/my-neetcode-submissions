import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(distances, (distance, point[0], point[1]))
        
        result = []
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            result.append([x, y])
        
        return result
