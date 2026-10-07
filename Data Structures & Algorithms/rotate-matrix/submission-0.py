class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        
        N = len(matrix)

        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]