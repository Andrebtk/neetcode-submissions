class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Memo = {}


        def dfs(amount):
            if amount == 0:
                return 0
            

            if amount in Memo:
                return Memo[amount]
            
            minNumCoins = 1e9
            for coin in coins:
                offset = amount - coin
                if offset >= 0:
                    newSteps = dfs(offset) + 1
                    minNumCoins = min(minNumCoins, newSteps)
            
            Memo[amount] = minNumCoins

            return minNumCoins
        

        val = dfs(amount)
        return -1 if val >= 1e9 else val