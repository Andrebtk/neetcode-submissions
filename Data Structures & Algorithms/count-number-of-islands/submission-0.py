class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMN = len(grid), len(grid[0])
        nbIslands = 0

        for r in range(ROWS):
            for c in range(COLUMN):
                if grid[r][c] == "1":
                    # We do a dfs

                    def dfs(grid, r, c, ROWS, COLUMN):
                        if min(r, c) < 0 or r >= ROWS or c >= COLUMN or grid[r][c] == "0":
                            return

                        grid[r][c] = "0"
                        dfs(grid, r + 1, c, ROWS, COLUMN)
                        dfs(grid, r - 1, c, ROWS, COLUMN)
                        dfs(grid, r, c + 1, ROWS, COLUMN)
                        dfs(grid, r, c - 1, ROWS, COLUMN)

                    dfs(grid, r, c, ROWS, COLUMN)
                    nbIslands += 1

        return nbIslands


