class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        memo = [[-1] * COLUMNS for _ in range(ROWS)]

        def aux(r, c):
            if r >= ROWS or c >= COLUMNS:
                return 9999999
            
            if r == ROWS - 1 and c == COLUMNS - 1:
                return grid[r][c]
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = min(aux(r + 1, c), aux(r, c + 1)) + grid[r][c]
            return memo[r][c]

        return aux(0, 0)