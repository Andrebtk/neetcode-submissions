class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        maxArea = 0


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:

                    def dfs(r,c):

                        if min(r,c) < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                            return 0
                        grid[r][c] = 0

                        nbLeft = dfs(r-1, c)
                        nbRight = dfs(r+1, c)
                        nbBottom = dfs(r, c-1)
                        nbTop = dfs(r, c+1)

                        return 1 + nbLeft + nbRight + nbTop + nbBottom
                    
                    nb = dfs(r,c)
                    maxArea = max(nb, maxArea)
        
        return maxArea