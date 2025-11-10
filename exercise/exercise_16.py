class Board:
    """
    Class representing a Sudoku board and its solving logic.
    """

    def __init__(self, board):
        """Initialize the Board with a 9x9 grid."""
        self.board = board

    def __str__(self):
        """Return a string representation of the board with '*' for empty cells."""
        board_str = ""
        for row in self.board:
            row_str = [str(cell) if cell != 0 else "*" for cell in row]
            board_str += " ".join(row_str) + "\n"
        return board_str

    def find_empty_cell(self):
        """Find the first empty cell in the board."""
        for row_index, row_contents in enumerate(self.board):
            try:
                col_index = row_contents.index(0)
                return row_index, col_index
            except ValueError:
                continue
        return None

    def is_valid_in_row(self, row, number):
        """Check if the number is not already in the given row."""
        return number not in self.board[row]

    def is_valid_in_col(self, col, number):
        """Check if the number is not already in the given column."""
        return all(self.board[row][col] != number for row in range(9))

    def is_valid_in_square(self, row, col, number):
        """Check if the number is not already in the 3x3 square containing (row, col)."""
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == number:
                    return False
        return True

    def is_valid_placement(self, cell, number):
        """Check if placing a number in a cell is valid according to Sudoku rules."""
        row, col = cell
        row_valid = self.is_valid_in_row(row, number)
        col_valid = self.is_valid_in_col(col, number)
        square_valid = self.is_valid_in_square(row, col, number)
        return all([row_valid, col_valid, square_valid])

    def solve(self):
        """Solve the Sudoku board using backtracking."""
        empty_cell = self.find_empty_cell()
        if empty_cell is None:
            return True

        for guess in range(1, 10):
            if self.is_valid_placement(empty_cell, guess):
                row, col = empty_cell
                self.board[row][col] = guess
                if self.solve():
                    return True
                self.board[row][col] = 0  # backtrack
        return False


def solve_sudoku(board):
    """Solve a Sudoku puzzle and print the initial and solved boards."""
    game_board = Board(board)
    print(f"Puzzle to solve:\n{game_board}")
    if game_board.solve():
        print(f"Solved puzzle:\n{game_board}")
    else:
        print("The provided puzzle is unsolvable.")
    return game_board


if __name__ == "__main__":
    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5],
    ]

    solve_sudoku(puzzle)
