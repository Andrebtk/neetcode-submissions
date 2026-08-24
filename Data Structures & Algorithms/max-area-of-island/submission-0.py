class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    # We have a land, so dfs to find the length
                    
                    def dfs(grid, r, c):

                        if min(r, c) < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == 0:
                            return 0
                        
                        grid[r][c] = 0
                        
                        currArea = 1
                        currArea += dfs(grid, r + 1, c)
                        currArea += dfs(grid, r - 1, c)
                        currArea += dfs(grid, r, c + 1)
                        currArea += dfs(grid, r, c - 1)
                        
                        return currArea

                    area = dfs(grid, r, c)
                    maxArea = max(maxArea, area) 
        return maxArea