


theBoard = {
        'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
        'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
        'low-l': ' ', 'low-m': ' ', 'low-r': ' '
}


def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

entry = input('enter X or O: ')
one = entry.upper()
print('player one entered ' + one)

turn = one
for i in range(9):
    printBoard(theBoard)
    move = input('its ' + turn + ' turn.....so hurry up: ')
    print()
    print()
    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)


