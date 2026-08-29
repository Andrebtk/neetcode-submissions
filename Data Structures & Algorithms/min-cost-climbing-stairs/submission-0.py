class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        memo = [-1] * (n + 1) 

        def aux(i):
            if i >= n:
                return 0

            if memo[i] == -1:
                memo[i] = min(aux(i + 1), aux(i + 2)) + cost[i]
                
            return memo[i]

        return min(aux(0), aux(1))