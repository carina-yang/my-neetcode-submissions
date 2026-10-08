class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [sorted_intervals[0]]

        for j in range(1, len(sorted_intervals)):
            if res[-1][1] >= sorted_intervals[j][0]:
                res[-1][1] = max(sorted_intervals[j][1], res[-1][1])
            else:
                res.append(sorted_intervals[j])
        
        return res
