class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]
        if startColor == color:
            return image
        

        def dfs(image, r, c, color):
            ROWS, COL = len(image), len(image[0])
            if min(r, c) < 0 or r >= ROWS or c >= COL or image[r][c] != startColor:
                return image
            
            if image[r][c] == startColor:
                image[r][c] = color
            else:
                return image
            
            dfs(image, r + 1, c, color)
            dfs(image, r - 1, c, color)
            dfs(image, r, c + 1, color)
            dfs(image, r, c - 1, color)

            return image
        

        return dfs(image, sr, sc, color)