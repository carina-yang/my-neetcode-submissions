class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0 
        max_profit = 0 
        
        for i in range(1, len(prices)): 
            if prices[i] < prices[left]: 
                left = i
            else:
                max_profit = max(max_profit, prices[i] - prices[left]) 
        
        return max_profit