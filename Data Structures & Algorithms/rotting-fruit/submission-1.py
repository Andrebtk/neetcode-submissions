class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        nbFruitFresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    nbFruitFresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        time = 0
        while q and nbFruitFresh > 0:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLUMNS or grid[newR][newC] != 1:
                        continue

                    grid[newR][newC] = 2
                    q.append((newR, newC))
                    nbFruitFresh -= 1
            time += 1
        
        if nbFruitFresh > 0:
            return -1
        return time

