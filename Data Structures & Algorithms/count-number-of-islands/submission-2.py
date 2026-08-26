class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        nbIslands = 0
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1":
                    # We do a dfs

                    def dfs(grid, r, c):
                        
                        if min(r, c) < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == "0":
                            return
                        
                        grid[r][c] = "0"

                        dfs(grid, r + 1, c)
                        dfs(grid, r - 1, c)
                        dfs(grid, r, c + 1)
                        dfs(grid, r, c - 1)

                    
                    dfs(grid, r, c)
                    nbIslands += 1
        
        return nbIslands