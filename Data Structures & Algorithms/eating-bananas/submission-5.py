class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if self.findHours(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo
    
    def findHours(self, piles, eatingRate):
        hours = 0
        for pile in piles:
            hours += -(-pile // eatingRate)
            
        return hours
