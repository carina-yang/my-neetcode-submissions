class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        price = [INF] * n
        price[src] = 0

        for _ in range(k + 1):
            prev_price = price[:]

            for from_i, to_i, price_i in flights: # 1, 2, 200
                if prev_price[from_i] != INF and prev_price[from_i] + price_i < price[to_i]:
                    price[to_i] =  price_i + prev_price[from_i]
        
        return -1 if INF == price[dst] else price[dst]
            

            