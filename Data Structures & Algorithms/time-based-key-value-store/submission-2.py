class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []

        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: 
            return ""

        values = self.mp[key]   
        L = 0
        R = len(values) - 1

        result = ""
        while L <= R:
            mid = (L + R) // 2
            mid_time, mid_value = values[mid]
            if mid_time <= timestamp:
                result = mid_value
                L = mid + 1
            else:
                R = mid - 1
        
        return result
