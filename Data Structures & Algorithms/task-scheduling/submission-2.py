from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1
        
        maxHeap = []

        for task in counts:
            heapq.heappush(maxHeap, -counts[task])
        
        time = 0
        cooldown = deque()

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1

                if cnt != 0:
                    cooldown.append([cnt, time + n])
            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])
            
        return time 

            
            
