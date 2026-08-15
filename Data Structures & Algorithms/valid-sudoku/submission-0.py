class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hasDup = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in hasDup:
                        return False
                    else:
                        hasDup.add(board[i][j])

        for i in range(9):
            hasDup = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in hasDup:
                        return False
                    else:
                        hasDup.add(board[j][i])

        for  i in range(9):
            hasDup = set()
            for x in range(3):
                for y in range(3):
                    row = (i // 3) * 3 + x
                    col = (i % 3) * 3 + y
                    if board[row][col] != ".":
                        if board[row][col] in hasDup:
                            return False
                        else:
                            hasDup.add(board[row][col])

        return True

                    