class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[-1] * n for i in range(m)]

        def aux(r, c, m, n):
            if r >= m or c >= n:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            if r == m - 1 and c == n - 1:
                return 1
            
            cache[r][c] = aux(r + 1, c, m, n) + aux(r, c + 1, m, n)

            return cache[r][c]
        

        return aux(0, 0, m, n)