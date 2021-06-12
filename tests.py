import unittest
from main import Board

class TestBoard(unittest.TestCase):

    def test_init_board(self):
        board = Board(['X', 'O'], empty_square='a')

        board.squares = ['a']*9
        board.current_player = 'X'
        board.players = ['X', 'O']
        board.empty_square = 'a'

    def test_move(self):

        board = Board(['X', 'O'], empty_square='a')
        board.squares = ['O', 'X', 'O', 'O', ' ', ' ', 'O', 'X', 'O' ]
        board.move('5')
        self.assertEqual(board.squares, ['O', 'X', 'O', 'O', ' ', 'X', 'O', 'X', 'O' ])



    def test_winning_board(self):
        board = Board(['X', 'O'])
        board.squares = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(board.has_won())

        board.squares = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.assertTrue(board.has_won())

        board.squares = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X' ]
        self.assertTrue(board.has_won())

        board.squares = ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X' ]
        self.assertFalse(board.has_won())

        board.squares = [' ', 'X', 'O', ' ', 'O', ' ', ' ', 'X', 'X' ]
        self.assertFalse(board.has_won())

        board.squares = [' ', ' ', 'O', ' ', 'O', 'O', ' ', 'X', 'O' ]
        self.assertTrue(board.has_won())

        board.squares = ['O', 'X', 'O', ' ', 'O', ' ', ' ', 'X', 'O' ]
        self.assertTrue(board.has_won())

        board.squares = ['O', 'X', 'O', 'O', ' ', ' ', 'O', 'X', 'O' ]
        self.assertTrue(board.has_won())

    def test_start_player(self):
        board = Board(['X', 'O'])

        self.assertEqual(board.current_player, 'X')

    
    def test_next_player(self):

        board = Board(['X', 'O'])

        board.next_player()
        self.assertEqual(board.current_player, 'O')
        board.next_player()
        self.assertEqual(board.current_player, 'X')
        board.next_player()
        self.assertEqual(board.current_player, 'O')
        
        board_three_players = Board(['X', 'O', 'Y'])

        board_three_players.next_player()
        self.assertEqual(board_three_players.current_player, 'O')
        board_three_players.next_player()
        self.assertEqual(board_three_players.current_player, 'Y')
        board_three_players.next_player()
        self.assertEqual(board_three_players.current_player, 'X')

    def test_valid_move(self):

        board = Board(['X', 'O'])
        board.squares = [' ', 'X', 'O', ' ', 'O', ' ', ' ', 'X', 'X' ]

        self.assertFalse(board.valid_move('a'))
        self.assertFalse(board.valid_move('!'))
        self.assertFalse(board.valid_move('1'))
        self.assertFalse(board.valid_move('11'))
        self.assertFalse(board.valid_move('2'))
        self.assertFalse(board.valid_move('qwertzuterwrtzr'))
        self.assertTrue(board.valid_move('0'))
        self.assertTrue(board.valid_move('3'))
        self.assertTrue(board.valid_move('5'))
        self.assertTrue(board.valid_move('6'))

    def test_is_full(self):
        board = Board(['X', 'O'], 'a')
        board.squares = ['X', 'X', 'O', ' ', 'O', 'a', 'O', 'X', 'X' ]
        self.assertFalse(board.is_full())

        board.squares = ['X', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'X' ]
        self.assertTrue(board.is_full())


        

if __name__ == '__main__':
    unittest.main()