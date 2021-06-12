#!/usr/bin/python3

class Board():
    ''' Sets up the game board. Handles also the current player. Checks if there is a win. '''

    def __init__(self, players, empty_square=' '):
        self.empty_square = empty_square
        self.players = players
        self.current_player = players[0]
        self.squares = [empty_square]*9

    
    @staticmethod
    def map_input(input):
        ''' Change the input from the numpad into indices of the squares. '''
        numpad_to_indices = {7:0, 8:1, 9:2, 4:3, 5:4, 6:5, 1:6, 2:7, 3:8}
        return numpad_to_indices[int(input)]

    
    def valid_move(self, square):
        ''' Checks if a move given by the player is valid on the current board. '''

        try:
            square = int(square)
        except ValueError as e:
            print('Give a number.')
            return False

        if square >= len(self.squares):
            print('Out of bounds.')
            return False

        if self.squares[square] in self.players:
            print('Already occupied.')
            return False
        
        return True

    
    def next_player(self):
        ''' Sets the next player as the current player. Supports more than one player. '''
        
        ix = self.players.index(self.current_player)
        # to get a cyclical index selection take the mod of the number of players
        next_ix = ( ix + 1 ) % len(self.players)
        self.current_player = self.players[next_ix]

        return self.current_player


    def move(self, square):
        ''' Places the move from the current player on the board. '''
        
        self.squares[int(square)] = self.current_player

        return True

    def is_full(self):
        ''' Checks if the board is full. The game ends. '''

        return self.empty_square not in self.squares

    def has_won(self):
        ''' Checks if the current player has won the game after the player has made his move. '''

        return (self.squares[0:3] != [self.empty_square]*3 and self.squares[0] == self.squares[1] == self.squares[2]) or \
               (self.squares[3:6] != [self.empty_square]*3 and self.squares[3] == self.squares[4] == self.squares[5]) or \
            (self.squares[6:9] != [self.empty_square]*3 and self.squares[6] == self.squares[7] == self.squares[8]) or \
                ([self.squares[0], self.squares[3], self.squares[6]] != [self.empty_square]*3 and self.squares[0] == self.squares[3] == self.squares[6]) or \
                ([self.squares[1], self.squares[4], self.squares[7]] != [self.empty_square]*3 and self.squares[1] == self.squares[4] == self.squares[7]) or \
                ([self.squares[2], self.squares[5], self.squares[8]] != [self.empty_square]*3 and self.squares[2] == self.squares[5] == self.squares[8]) or \
                ([self.squares[2], self.squares[4], self.squares[6]] != [self.empty_square]*3 and self.squares[2] == self.squares[4] == self.squares[6]) or \
                ([self.squares[0], self.squares[4], self.squares[8]] != [self.empty_square]*3 and self.squares[0] == self.squares[4] == self.squares[8])



    def __str__(self):
        ''' Pretty representation of the board class. '''

        line1 = f'{self.squares[0]} | {self.squares[1]} | {self.squares[2]}'
        line2 = f'{self.squares[3]} | {self.squares[4]} | {self.squares[5]}'
        line3 = f'{self.squares[6]} | {self.squares[7]} | {self.squares[8]}'
        between = f'-'*9

        return '\n'.join([line1, between, line2, between, line3])


if __name__ == '__main__':
    players = ['X', 'O']
    board = Board(players)

    print(board)
    print()
    while not ( board.has_won() or board.is_full() ):

        valid_move = False
        while not valid_move:
            numpad_input = input(f'Player {board.current_player}. What is your move (use numpad: 1-8 - upperleft is 7)? ')
            square = board.map_input(numpad_input)
            valid_move = board.valid_move(square)
            if valid_move:
                board.move(square)
            if not board.has_won():
                board.next_player()

        print()
        print(board)

    if board.has_won():    
        print(f'Player {board.current_player} has won!')
    else:
        print(f'It is a tie.')
