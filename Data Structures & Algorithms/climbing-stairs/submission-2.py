class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def aux(i):
            if i >= n:
                return 1
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = aux(i + 1) + aux(i + 2)
            return memo[i]

        return aux(1)