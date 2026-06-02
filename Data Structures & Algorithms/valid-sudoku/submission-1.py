class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            col = set()
            square = set()
            for j in range(len(board)):
                if board[j][i] != '.' and board[j][i] in col:
                    return False
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row_index = (i // 3) * 3 + j // 3
                col_index = (i % 3) * 3 + j % 3
                if board[row_index][col_index] != '.' and board[row_index][col_index] in square:
                    return False
                col.add(board[j][i])
                row.add(board[i][j])
                square.add(board[row_index][col_index])
        return True