class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:

                    curArea = 0
                    def dfs(grid, r, c, visited):
                        if min(r, c) < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == 0 or (r, c) in visited:
                            return 0
                        
                        visited.add((r, c))
                        local = 1
                        local += dfs(grid, r + 1, c, visited)
                        local += dfs(grid, r - 1, c, visited)
                        local += dfs(grid, r, c + 1, visited)
                        local += dfs(grid, r, c - 1, visited)
                        
                        return local

                    curArea = dfs(grid, r, c, visited)
                    maxArea = max(maxArea, curArea)

        return maxArea