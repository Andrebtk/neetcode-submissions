class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        memo = [-1] * (N + 1)


        def aux(i):
            if i >= N:
                return 0
            
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(aux(i + 1), aux(i + 2))
            return memo[i]
        

        return min(aux(0), aux(1))