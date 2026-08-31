class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(obstacleGrid), len(obstacleGrid[0])
        
        memo = [[-1] * COLUMNS for i in range(ROWS)]

        def aux(r,c):
            if r >= ROWS or c >= COLUMNS or obstacleGrid[r][c] == 1:
                return 0
            
            if r == ROWS -1 and c == COLUMNS - 1:
                return 1

            if memo[r][c] != -1:
                return memo[r][c]

            memo[r][c] = aux(r + 1, c) + aux(r, c + 1)
            return memo[r][c]
        
        return aux(0, 0)