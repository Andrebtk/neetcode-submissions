class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = float('inf')
        maxProf = 0


        for elem in prices:
            minBuy = min(minBuy, elem)
            prof = elem - minBuy
            maxProf = max(maxProf, prof)
        

        return maxProf