class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for i in range(m)]


        def aux(r, c):
            if r >= m or c >= n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if memo[r][c] != -1:
                return memo[r][c]

            memo[r][c] = aux(r + 1, c) + aux(r, c + 1)
            return memo[r][c]
            
        return aux(0, 0)