import unittest
from noughts_crosses import GameBoard
from StringIO import StringIO

def get_gameboard_display(game_board):
    out = StringIO()
    game_board.display(out=out)
    return out.getvalue()

# TODO(alex): Add three more test cases. Test
# edge cases
class NoughtsCrossesGame(unittest.TestCase):
   def test_play_game(self):
       # John (player 0) and Mary (player 1) decided they 
       # might play a game of noughts and crosses the
       # game board is displayed in front of them
       gameboard = GameBoard()
       expected_gameboard = " | | \n-----\n | | \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # John, the noughts player is invited to 
       # provide his choice. He choose the top
       # left corner by providing input 0 0
       gameboard.play_move(0, 0, 0)
       expected_gameboard = "O| | \n-----\n | | \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # Mary believes the key to noughts and crosses
       # success is to secure the middle of the board
       # and places her cross in the middle providing
       # input 1 1
       gameboard.play_move(1, 1, 1)
       expected_gameboard = "O| | \n-----\n |X| \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # John marches along the top of the board
       # and places his choice at 0 1
       gameboard.play_move(0, 0, 1)
       expected_gameboard = "O|O| \n-----\n |X| \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # Mary blocks John's potential for a win 
       # by placing a cross at 0 2
       gameboard.play_move(1, 0, 2)
       expected_gameboard = "O|O|X\n-----\n |X| \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # John frustrated with Mary's move looks
       # to sieze the win again by choosing 1 0
       gameboard.play_move(0, 1, 0)
       expected_gameboard = "O|O|X\n-----\nO|X| \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # Mary is feeling the heat and checks
       # whether John has won
       self.assertNotEqual(gameboard.winner, 0)

       # With the relief that John hasn't won
       # Mary studies the board and finds she
       # can win! she places a cross at 2 0
       gameboard.play_move(1, 2, 0)
       expected_gameboard = "O|O|X\n-----\nO|X| \n-----\nX| | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # Mary has won!
       self.assertEqual(gameboard.winner, 1)

       # the game finishes and they go grab some food

class NoughtsCrossesBoard(unittest.TestCase):
    def test_displays_game_board(self):
        expected_game_board = " | | \n-----\n | | \n-----\n | | \n"
        gameboard = GameBoard()
        output = get_gameboard_display(gameboard)
        self.assertEqual(output, expected_game_board)

    def test_first_move_by_noughts_on_game_board(self):
        gameboard = GameBoard()

        legal_move = gameboard.play_move(0, 1, 1)
        self.assertEqual(legal_move, True)

        expected_game_board = " | | \n-----\n |O| \n-----\n | | \n"
        output = get_gameboard_display(gameboard)
        self.assertEqual(output, expected_game_board)

    def test_no_winner_when_game_starts(self):
        gameboard = GameBoard()
        self.assertEqual(gameboard.winner, None)

    def test_crosses_winner_using_top_row(self):
        gameboard = GameBoard()
        gameboard.play_move(1, 0, 0)
        gameboard.play_move(1, 0, 1)
        gameboard.play_move(1, 0, 2)
        self.assertEqual(gameboard.winner, 1)

if __name__ == '__main__':
    unittest.main()
