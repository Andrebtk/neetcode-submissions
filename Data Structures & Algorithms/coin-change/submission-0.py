class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}


        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            val = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    newMin = 1 + dfs(amount - coin)
                    val = min(val, newMin)
            
            memo[amount] = val
            return val

        data = dfs(amount)
        return -1 if data >= 1e9 else data



