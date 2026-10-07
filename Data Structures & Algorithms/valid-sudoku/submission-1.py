class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valRow = defaultdict(set)
        valCol = defaultdict(set)
        valGrid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                
                val = board[i][j]

                if (val in valRow[i] or val in valCol[j] or val in valGrid[(i // 3, j // 3)]):
                    return False
                
                valRow[i].add(val)
                valCol[j].add(val)
                valGrid[(i // 3, j // 3)].add(val)

        return True