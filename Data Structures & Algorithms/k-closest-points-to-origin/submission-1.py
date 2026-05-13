import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(distances, (-1 * distance, point[0], point[1]))

            if len(distances) > k:
                heapq.heappop(distances)
        
        return [[element[1], element[2]] for element in distances]
