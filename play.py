from tictactoe import TicTacToe
from exception import NonEmptySpotError

ttt = TicTacToe()

print('===============')
print('PY-TAC-TOE GAME')
print('===============')

while True:
    print('>> Current player: {0}'.format(ttt.player))
    print('>> Current turn: {0}'.format(ttt.turn))

    print(ttt.render())

    currentState = ttt.checkIfWon()

    if currentState == ttt.DRAW:
        print('=== GAME OVER ===================')
        print('DRAW! No one wins!')
        break
    if currentState == ttt.X_WIN:
        print('=== GAME OVER ===================')
        print('X wins!')
        break
    if currentState == ttt.O_WIN:
        print('=== GAME OVER ===================')
        print('O wins!')
        break

    try:
        coords = input('Position (a-c|1-3): ')
        position = ttt.parseCoords(coords)
        ttt.setPiece(ttt.player, position)
        ttt.nextTurn()

    except NonEmptySpotError:
        print('\n=== ERROR ===================')
        print('Position already taken\n')
    except ValueError:
        print('\n=== ERROR ===================')
        print('Please input a valid position number\n')
    except IndexError:
        print('\n=== ERROR ===================')
        print('Position out of bounds of the board\n')
