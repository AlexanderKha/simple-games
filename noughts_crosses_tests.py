import unittest
import noughts_crosses
from noughts_crosses import GameBoard
from StringIO import StringIO

def get_gameboard_display(game_board):
    out = StringIO()
    game_board.display(out=out)
    return out.getvalue()

''''''''''''''''''''''''''''''''''''''
'                                    '
' User Story 1 - Draw Game Scenario  '
'                                    '
'             O | X | O              '
'             O | X | X              '
'             X | O | O              '
'                                    '
''''''''''''''''''''''''''''''''''''''

# Tom & Jerry loads the Noughts and Crosses web page.

# He is greeted by a noughts and crosses board with a
# window on the right telling the rules of the game.

# The game prompts player one to make a move in which
# Tom marks the top left corner. The website responds by
# having the board presenting a “O”.

# The game now prompts player two to make a move in which
# Jerry marks the middle top. The website responds by having
# the board presenting a “X” in that position

# Tom feeling cheeky tries to place a move on top of Jerry’s
# move in the middle top. The website responds by notifying
# Jerry that the move is illegal and to try again. Feeling
# down Tom Marks the bottom right corner instead. Where the
# website responds with a “O” marking.

# Having no choice Jerry marks the middle box in order to
# prevent Tom from winning but to also set himself up.

# Tom counters by marking the bottom middle to prevent Jerry
# from winning whilst also setting himself up to win.

# Jerry having no choice is forced to counter by marking
# the bottom left box with a “X”.

# Tom counters with the top right corner to prevent Jerry from winning.

# Likewise Jerry marks the middle right realising the game is leading to a draw

# Tom marks the final mark with on the middle left box with a “O” where the
# game has now stated the sad obvious outcome. The game is a draw.



''''''''''''''''''''''''''''''''''''''
'                                    '
' User Story 2 - Win Game Scenario   '
'                                    '
'             O |   | X              '
'               | X |                '
'             O | O | O              '
'                                    '
''''''''''''''''''''''''''''''''''''''

# Tom & Jerry loads the Noughts and Crosses Web Page

# They are greeted by a noughts and crosses board with a
# window on the right telling the rules of the game.

# The game prompts player one to make a move.
# Tom being player one marks the top left corner.
# The website responds with a "O" marking in the corresponding
# corner.

# Jerry being player two marks the top right of the grid.
# The website responds by updating the grid with a "X" in the
# top right corner.

# Tom feeling cunning, marks the bottom right corner to set up
# a diagonal move.

# Jerry forced to prevent Tom from winning marks the middle grid.

# Tom sets up the final blow as well as preventing Jerry from
# winning by marking the bottom left.

# Jerry in dispair realises regardless of what move he makes,
# he has lost the game. So he hesitantly clicks and selects the
# middle left to prolong the game.

# Tom cheerfully picks the bottom middle to complete 3 "0" in a
# row. Where the website announces player one as the winner



''''''''''''''''''''''''''''''''''''''
'                                    '
' User Story 3 - Lose Game Scenario  '
'                                    '
'             O | O | X              '
'               | O | O              '
'             X | X | X              '
'                                    '                                  '
''''''''''''''''''''''''''''''''''''''

# Tom & Jerry loads the Noughts and Crosses Web Page

# They are greeted by a noughts and crosses board with a
# window on the right telling the rules of the game.

# The game prompts player one to make a move.
# Tom being player one marks the top middle if the board.
# The website responds with a "O" marking in the corresponding
# section.

# Jerry being player two decides to mark the bottom left of the
# grid. The website responds by updating the grid with a "X" in the
# bottom left corner.

# Tom wanting a quick game, marks the top left corner to set up
# a straight move.

# Jerry feels forced to prevent Tom from winning and marks the
# top right.

# Tom sees that Jerry by preventing him from winning has set up a
# move for the middle. As a result Tom marks the middle of the board.

# Jerry in his haste mistakenly doesn't prevent Jerry's setup down
# the middle vertical and picks the bottom right corner. As a result
# he is eagerly anticipating Tom's move.

# Tom too focused on seeing Jerry's setup for a double win doesn't
# realise that he has a winning move down the middle. Instead he
# rushes to stop Jerry from making a move by selecting the middle right.

# Jerry relieved, selects the middle bottom to win the game by
# creating a straight on the bottom. The website announces player two
# as the winner.



''''''''''''''''''''''''''''''''''''''
'                                    '
' User Story 4 - Page Refresh        '
' Game Scenario                      '
'                                    '
''''''''''''''''''''''''''''''''''''''



# Original Functional Tests for testing console version
# of Noughts and Crosses
class NoughtsCrossesGameConsoleVersion(unittest.TestCase):
   def test_play_game(self):
       # John (player 0) and Mary (player 1) decided they 
       # might play a game of noughts and crosses the
       # game board is displayed in front of them
       gameboard = GameBoard()
       expected_gameboard = " | | \n-----\n | | \n-----\n | | \n"
       output = get_gameboard_display(gameboard)
       self.assertEqual(output, expected_gameboard)

       # John accidentally enters wrong input at the prompt
       # by doing so he hits enter and inputs an empty command.
       gameboard.play_move(0, "", "")
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


       # Mary accidentally hits the enter button leading
       # to a no input for her move.
       gameboard.play_move(1, "", "")
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
        
    def test_legal_moves(self):
        gameboard = GameBoard()
        
        illegal_move = gameboard.play_move(0, 9, 9)
        self.assertEqual(illegal_move, False)
        
        illegal_move = gameboard.play_move(1, 9, 9)
        self.assertEqual(illegal_move,  False)
        
        illegal_move = gameboard.play_move(0, "", "")
        self.assertEqual(illegal_move, False)
        
        illegal_move = gameboard.play_move(1, "", "")
        self.assertEqual(illegal_move, False)
        

    # Test the user input of an actual game
    # Need to investigate how to simulate user input
    # and how to check / test actual printed statements
    # i.e. the output
    #
    # unittest mock and @patch may be a lead
    
# class NoughtsCrossesBoardUserInput(unittest.TestCase):
#   def test_userinput_game(self):
#        noughts_crosses.play_game()
   
    
if __name__ == '__main__':
    unittest.main()
