class Board():
    def __init__(self,board_size):
        self.board_size=board_size
        self._initialize_board()

    def _initialize_board(self):
        self.board = [[(i, j) for i in range(self.board_size)]
                      for j in range(self.board_size)] 

    def __repr__(self):
        """
        Print the board in a pretty format.
        """
        # Let's initialize the top row of column numbers first.
        board_output = '    ' + '   '.join(str(num) for
                num in range(self.board_size)) + '\n'

        for row_idx, row in enumerate(self.board):
            board_output += ' {} '.format(row_idx)
            for col_idx, col in enumerate(row):
                if col in [' X ', ' O ']:
                    if col_idx != self.board_size - 1:
                        board_output += col + '|'
                    else:
                        board_output += col
                else:
                    if col_idx != self.board_size - 1:
                        board_output += ' ' * 3 + '|'
                    else:
                        board_output += ' ' * 3
            board_output += '\n'
            if row_idx != self.board_size - 1:
                board_output += ' ' * 3
                board_output += '--' * self.board_size * 2
                board_output += '\n'

        return board_output

b1=Board(3)
b1.board_size = int(input("What size board would you like to play on today? "))
b1._initialize_board()
print(b1.board)