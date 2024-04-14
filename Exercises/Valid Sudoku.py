from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Controllo per righe e colonne
        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in row:
                    return False
                if board[j][i].isdigit() and board[j][i] in col:
                    return False
                row[board[i][j]] = True
                col[board[j][i]] = True

        # Controllo per le sottomatrici 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = {}
                for m in range(3):
                    for n in range(3):
                        if board[i + m][j + n].isdigit() and board[i + m][j + n] in subgrid:
                            return False
                        subgrid[board[i + m][j + n]] = True

        return True

sol = Solution()
board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
print(sol.isValidSudoku(board))
