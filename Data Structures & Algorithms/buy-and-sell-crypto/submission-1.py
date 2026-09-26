class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0

        for elem in prices:
            min_buy = min(min_buy, elem)
            profit = elem - min_buy
            max_profit = max(profit, max_profit)
        
        return max_profit