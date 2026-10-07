class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])


        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = 0, 0
        current = 0


        output = []
        
        while len(output) < (M * N):
            output.append(matrix[r][c])

            matrix[r][c] = 101
            dr, dc = direction[current]
            
            new_r, new_c = r + dr, c + dc

            if not (0 <= new_r < M and 0 <= new_c < N and matrix[new_r][new_c] != 101):
                current = (current + 1) % 4
                dr, dc = direction[current]
            

            r, c = r + dr, c + dc
        
        return output

