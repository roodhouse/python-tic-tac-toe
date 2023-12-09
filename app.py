board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board():
    for row in board:
        print('| {} | {} | {} |'.format(row[0], row[1], row[2]))

print_board()

x = True
o = False

game_on = True

def choice():
    row = input('Enter row number: ')
    col = input('Enter column number: ')
    
    row = int(row) - 1
    col = int(col) - 1
    if row < 0 or col < 0 or row > 2 or col > 2:
            print('invalid location')
            choice()
    else:
        if board[row][col] == '-':
                if x:
                    board[row][col] = 'x'
                    place = [row, col]     
                    return place
                else:
                    board[row][col] = 'o'
                    place = [row, col]     
                    return place
        else:
            print('location taken')
            choice()

while game_on:
    if x:
        print('x Turn')
        choice()
        x = False
    else:
        print('o Turn')
        choice()
        x = True
    print_board()