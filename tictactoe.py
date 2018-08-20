from exception import NonEmptySpotError
from textwrap import dedent

class TicTacToe:
    DRAW = 0
    X_WIN = 1
    O_WIN = 2

    def __init__(self):
        self._gameboard = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self._rows = [0, 0, 0]
        self._cols = [0, 0, 0]
        self._diag = [0, 0]
        self._player = 'X'
        self._turn = 1

    @property
    def turn(self):
        return self._turn
        
    @property
    def player(self):
        return self._player

    def checkIfWon(self):
        if 3 in self._rows or 3 in self._cols or 3 in self._diag:
            return self.X_WIN
        if -3 in self._rows or -3 in self._cols or -3 in self._diag:
            return self.O_WIN
        if (self._turn > 9):
            return self.DRAW

    def parseCoords(self, coords):
        splitCoords = list(coords)
        return (ord(splitCoords[0]) - 97, int(splitCoords[1]) - 1)
    
    def setPiece(self, piece, position):
        if self._gameboard[position[0]][position[1]] == ' ':
            self._gameboard[position[0]][position[1]] = piece

            self._rows[position[0]] += (1 if self._player == 'X' else -1) 
            self._cols[position[1]] += (1 if self._player == 'X' else -1)
            # fix diagonal checkings
            if (position in [(0, 0), (1, 1), (2, 2)]):
                self._diag[0] += (1 if self._player == 'X' else -1)
            if (position in [(0, 2), (1, 1), (2, 0)]):
                self._diag[1] += (1 if self._player == 'X' else -1)
        else:
            raise NonEmptySpotError()

    def nextTurn(self):
        self._player = ('O' if self._player == 'X' else 'X')
        self._turn += 1

    def render(self):
        grid = dedent("""
           1   2   3
        a  {0} | {1} | {2} """).format(*self._gameboard[0])

        grid += dedent("""
          -----------
        b  {0} | {1} | {2} """).format(*self._gameboard[1])

        grid += dedent("""
          -----------
        c  {0} | {1} | {2} \n""").format(*self._gameboard[2])

        return grid