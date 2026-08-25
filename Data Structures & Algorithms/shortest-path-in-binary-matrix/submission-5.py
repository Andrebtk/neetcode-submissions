class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return -1
            
        visited = set()
        q = deque()
        q.append((0, 0))
        visited.add((0,0))

        length = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLUMNS - 1:
                    return length
                
                directions = [[1,0], [0,1], [-1, 0], [0, -1],
                                [1,1], [-1,-1], [1,-1], [-1, 1]]
                
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLUMNS or grid[newR][newC] == 1 or (newR, newC) in visited:
                        continue
                    q.append((newR, newC))
                    visited.add((newR, newC))
            length += 1
        
        return -1