
def letter():
    userone = input('User enter X or O: ').upper()
    if userone not in ('X', 'O'):
        print('Enter an X or an O, por favor')
        letter()
    else:
        print('User 1 entered ' + userone)
        return userone

userone = letter()

usertwo = ''
if userone == 'X':
    usertwo = 'O'
else:
    usertwo = 'X'

print()
print('user one is: ' + userone)
print('user two is: ' + usertwo)
print()

board = []

for x in range(0, 3):
    board.append('[ ]' * 3)

def makeboard(list):
#    for colNum, colBox in enumerate(list, start = 1):
#        print(str(colNum) + '  ' + str(colNum))
    print ('    1     2     3')
    for rowNum, rowBox in enumerate(list, start = 1):
        print(str(rowNum) + ' ' + ' '.join(rowBox))
        print()

makeboard(board)

print(len(board))

def taketurn(turn):
    print('IT IS ' + turn + '\'S TURN...')
    print('PICK YOUR COORDINATES, ' + turn)
    row = input('ROW: ')
    #if row
    col = input('COLUMN: ')

turn = userone
taketurn(turn)






#      _   _
#     | | | |
#     | |_| |
#      \__, |
#      |___/
