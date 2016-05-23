"""
CHALLENGES:
    - Create UI-based version of game
    - Create web-based version of game
"""
from sys import stdout

class GameBoard():
    """ Noughts and Crosses game board is implemented using a list
    of length 9 for each spot on the gameboard. The indicies of the list
    are allocated one row at a time, from left to right, top to bottom.

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8

    Each spot on the gameboard can be accessed by a row and column index
    with the index starting at 0. So (0,1) corresponds to index 1 of the
    gameboard list.

    Noughts and crosses players are indexed by 0 and 1. 0 for the noughts
    player and 1 for the crosses player
    """
    _display_markers = {
        0: "O",
        1: "X",
        100: " "
    }
    _players = [0, 1]
    _valid_rows = _valid_cols = range(3)
    _winning_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self):
        """Create the game board and index players"""
        self._gameboard = [100] * 9
        self.winner = None

    def display(self, out=stdout):
        """Displays the gameboard visually to an output stream.
        Defaults to the standard output stream i.e. console output"""
        display_board = [self._display_markers[pos] for pos in self._gameboard]
        display = """%s|%s|%s\n-----\n%s|%s|%s\n-----\n%s|%s|%s\n"""
        out.write(display % tuple(display_board))

    def play_move(self, player, row, col):
        """Places a move on the gameboard for a player. Returns
        whether the move made by a player was valid"""
        valid_move = row in self._valid_rows and col in self._valid_cols
        if player in self._players and valid_move:
            index = row * 3 + col
            if self._gameboard[index] == 100:
                self._gameboard[index] = player
                self.winner = self._check_winner()
                return True
            else:
                return False
        else:
            return False

    def _check_winner(self):
        """Check if there is a winner. Return one of three values
        0 if noughts has won
        1 if crosses has won
        None if no one has won"""
        for combo in self._winning_combos:
            score = sum([self._gameboard[x] for x in combo])
            if score == 3:
                return 1
            elif score == 0:
                return 0

        return None

def play_game():
    # starts a game of noughts and crosses
    print """
    Let's play noughts and crosses!

    There is a 3x3 gameboard displayed in the
    console. There are two players, player 0
    (noughts) and player 1 (crosses). Each will
    take turns specifying their move on the board.

    To choose a spot on the gameboard enter the row
    0,1 or 2 followed by a space and then the
    column 0,1, or 2. Press ENTER to finalise your
    move. For example to select the middle spot
    on the gameboard enter 1 1 and then press
    ENTER.

    """

    # NOTE(steve): think abou maybe creating a 
    # game class that handles the game logic
    gb = GameBoard()
    current_player = 0
    remaining_moves = 9
    while gb.winner == None and remaining_moves:
        gb.display()

        print "\nPlayer %d, please make your move." % current_player
        move = raw_input("> ")
        print "\n"

        try:
            input_row, space, input_col = move
            row = int(input_row)
            col = int(input_col)
            if gb.play_move(current_player, row, col):
                remaining_moves -= 1
                if current_player:
                    current_player = 0
                else:
                    current_player = 1
            else:
                print "Invalid move!"
        except:
            print """Invalid move please enter row and column as integers with
            a single space inbetween!"""

    if gb.winner:
        print "Gameover! The winner is player %d!" % gb.winner
    else:
        print "Gameover! It is a draw!"

if __name__ == '__main__':
    play_game()