class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minDay = float('inf')
        maxProf = 0


        for p in prices:
            minDay = min(minDay, p)
            profit = p - minDay
            maxProf = max(maxProf, profit)

        return maxProf