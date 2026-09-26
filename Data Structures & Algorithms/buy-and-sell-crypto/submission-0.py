class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for elem in prices:
            min_price = min(elem, min_price)
            profit = elem - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit