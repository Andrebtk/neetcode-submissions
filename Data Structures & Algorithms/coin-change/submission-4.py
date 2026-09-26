class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        Memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            

            if Memo.get(amount) is not None:
                    return Memo[amount]

            minCoins = 1e9
            for coin in coins:
                offset = amount - coin

                if offset >= 0:
                    newSteps = 1 + dfs(offset)
                    minCoins = min(minCoins, newSteps)
            
            Memo[amount] = minCoins

            return minCoins

        val = dfs(amount)
        return -1 if val >= 1e9 else val