class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        Memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in Memo:
                return Memo[amount]
            

            minCoinUsed = float('inf')
            for coin in coins:
                offset = amount - coin
                if offset >= 0:
                    minCoinUsed = min(minCoinUsed, 1 + dfs(offset))
            
            Memo[amount] = minCoinUsed
            return minCoinUsed
        
        val = dfs(amount)
    
        return -1 if val >= float('inf') else val
