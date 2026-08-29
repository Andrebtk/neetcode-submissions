class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(obstacleGrid), len(obstacleGrid[0])

        cache = [[-1] * COLUMNS for i in range(ROWS)]

        def aux(r, c):
            if r >= ROWS or c >= COLUMNS:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            if r == ROWS - 1 and c == COLUMNS - 1:
                return 1
            
            cache[r][c] = aux(r + 1, c) + aux(r, c + 1)

            return cache[r][c]


        
        return aux(0, 0)