#!/usr/bin/python3

class Board():

    def __init__(self, players, empty_square=' '):
        self.empty_square = empty_square
        self.players = players
        self.current_player = players[0]
        self.squares = [empty_square]*9

    
    def valid_move(self, square):
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
        
        ix = self.players.index(self.current_player)
        # to get a cyclical index selection take the mod of the number of players
        next_ix = ( ix + 1 ) % len(self.players)
        self.current_player = self.players[next_ix]

        return self.current_player


    def move(self, square):

        # self.squares.insert(int(square), self.current_player)
        self.squares[int(square)] = self.current_player

        return True

    def is_full(self):

        return self.empty_square not in self.squares

    def has_won(self):

        return (self.squares[0:3] != [self.empty_square]*3 and self.squares[0] == self.squares[1] == self.squares[2]) or \
               (self.squares[3:6] != [self.empty_square]*3 and self.squares[3] == self.squares[4] == self.squares[5]) or \
            (self.squares[6:9] != [self.empty_square]*3 and self.squares[6] == self.squares[7] == self.squares[8]) or \
                ([self.squares[0], self.squares[3], self.squares[6]] != [self.empty_square]*3 and self.squares[0] == self.squares[3] == self.squares[6]) or \
                ([self.squares[1], self.squares[4], self.squares[7]] != [self.empty_square]*3 and self.squares[1] == self.squares[4] == self.squares[7]) or \
                ([self.squares[2], self.squares[5], self.squares[8]] != [self.empty_square]*3 and self.squares[2] == self.squares[5] == self.squares[8]) or \
                ([self.squares[2], self.squares[4], self.squares[6]] != [self.empty_square]*3 and self.squares[2] == self.squares[4] == self.squares[6]) or \
                ([self.squares[0], self.squares[4], self.squares[8]] != [self.empty_square]*3 and self.squares[0] == self.squares[4] == self.squares[8])



    def __str__(self):

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
            square = input(f'Player {board.current_player}. What is your move [0-{len(board.squares)-1}]? ')
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
