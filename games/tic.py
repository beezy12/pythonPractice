
userone = ''
def startingPiece():
    userone = input('User enter X or O: ').upper()
    if userone not in ('X', 'O'):
        print('Enter the right damn letter!')
        startingPiece()
    else:
        print('User 1 entered ' + userone)

startingPiece()

if 

board = []

for x in range(0, 3):
    board.append('[]' * 3)

def makeboard(list):
    for row in list:
        print(' '.join(row))

makeboard(board)
