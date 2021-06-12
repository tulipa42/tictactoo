#!/usr/bin/python3
from typing import List, Union

Player = str
Players = List[Player]
Numpad_Input = Union[int, str]


class Board():
    ''' Sets up the game board. Handles also the current player. Checks if there is a win. '''

    def __init__(self, players: Players, empty_square:str=' ') -> None:
        self.empty_square = empty_square
        self.players = players
        self.current_player = players[0]
        self.squares = [empty_square]*9
        self.numpad_to_indices = {7:0, 8:1, 9:2, 4:3, 5:4, 6:5, 1:6, 2:7, 3:8}
    
    def valid_move(self, square:Numpad_Input) -> bool:
        ''' Checks if a move given by the player is valid on the current board. '''        

        try:
            square = int(square)
        except ValueError as e:
            print('Give a number.')
            return False
            
        if square not in self.numpad_to_indices:
            print('Out of bounds.')
            return False

        if self.squares[self.numpad_to_indices[square]] in self.players:
            print('Already occupied.')
            return False
        
        return True

    
    def next_player(self) -> Player:
        ''' Sets the next player as the current player. Supports more than one player. '''
        
        ix = self.players.index(self.current_player)
        # to get a cyclical index selection take the mod of the number of players
        next_ix = ( ix + 1 ) % len(self.players)
        self.current_player = self.players[next_ix]

        return self.current_player


    def move(self, square:Numpad_Input) -> bool:
        ''' Places the move from the current player on the board. '''

        square = self.numpad_to_indices[int(square)]
        
        self.squares[square] = self.current_player

        return True

    def is_full(self) -> bool:
        ''' Checks if the board is full. The game ends. '''

        return self.empty_square not in self.squares

    def has_won(self) -> bool:
        ''' Checks if the current player has won the game after the player has made his move. '''

        return (self.squares[0:3] != [self.empty_square]*3 and self.squares[0] == self.squares[1] == self.squares[2]) or \
               (self.squares[3:6] != [self.empty_square]*3 and self.squares[3] == self.squares[4] == self.squares[5]) or \
            (self.squares[6:9] != [self.empty_square]*3 and self.squares[6] == self.squares[7] == self.squares[8]) or \
                ([self.squares[0], self.squares[3], self.squares[6]] != [self.empty_square]*3 and self.squares[0] == self.squares[3] == self.squares[6]) or \
                ([self.squares[1], self.squares[4], self.squares[7]] != [self.empty_square]*3 and self.squares[1] == self.squares[4] == self.squares[7]) or \
                ([self.squares[2], self.squares[5], self.squares[8]] != [self.empty_square]*3 and self.squares[2] == self.squares[5] == self.squares[8]) or \
                ([self.squares[2], self.squares[4], self.squares[6]] != [self.empty_square]*3 and self.squares[2] == self.squares[4] == self.squares[6]) or \
                ([self.squares[0], self.squares[4], self.squares[8]] != [self.empty_square]*3 and self.squares[0] == self.squares[4] == self.squares[8])



    def __str__(self) -> str:
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
        while valid_move == False:
            numpad_input = input(f'Player {board.current_player}. What is your move (use numpad: 1-8 - upperleft is 7)? ')
            valid_move = board.valid_move(numpad_input)
            if valid_move:
                board.move(numpad_input)
            if not board.has_won():
                board.next_player()

        print()
        print(board)

    if board.has_won():    
        print(f'Player {board.current_player} has won!')
    else:
        print(f'It is a tie.')
