class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nbFreshFruit = 0
        q = deque()


        ROWS, COLUMNS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    nbFreshFruit += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        direction = [[0,1], [1,0], [0, -1], [-1, 0]]
        time = 0

        while q and nbFreshFruit > 0:
            # we do a BFS on each rotten fruit
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for dr, dc in direction:
                    newR, newC = r + dr, c + dc
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLUMNS or grid[newR][newC] != 1:
                        continue
                    q.append((newR, newC))
                    grid[newR][newC] = 2
                    nbFreshFruit -= 1
                
            time += 1
        
        if nbFreshFruit > 0:
            return -1
        return time


                


