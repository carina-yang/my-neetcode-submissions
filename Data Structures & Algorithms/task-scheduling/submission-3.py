from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1

        max_freq = max(counts.values())
        num_max_freq = sum(1 for c in counts.values() if c == max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max_freq)

            
            
