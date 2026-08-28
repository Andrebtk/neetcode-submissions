class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = [-1] * (n + 1) 

        def aux(i):
            if i == 0:
                return 0
            
            if i == 1 or i == 2:
                return 1
            
            if memo[i] == -1:
                memo[i] = aux(i-1) + aux(i-2) + aux(i-3)

            return memo[i]

        return aux(n)  