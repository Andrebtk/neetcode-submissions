class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        output = []
        r, c = 0, 0

        
        while len(output) < (M * N):
            
            output.append(matrix[r][c])
            matrix[r][c] = 101


            # next direction
            dr, dc = directions[direction]
            next_r, next_c = r + dr, c + dc

            if not( 0 <= next_r < M and 0 <= next_c < N and matrix[next_r][next_c] != 101):
                direction = (direction + 1) % 4
                dr, dc = directions[direction]
            
            r, c = r + dr, c + dc 
                 

        return output




