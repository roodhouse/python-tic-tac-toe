board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def print_board():
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))


print_board()

x = True
o = False

game_on = True


def choice():
    row = input("Enter row number: ")
    col = input("Enter column number: ")

    row = int(row) - 1
    col = int(col) - 1
    if row < 0 or col < 0 or row > 2 or col > 2:
        print("invalid location")
        choice()
    else:
        if board[row][col] == "-":
            if x:
                board[row][col] = "x"
                place = [row, col]
                return place
            else:
                board[row][col] = "o"
                place = [row, col]
                return place
        else:
            print("location taken")
            choice()


def check_winner():
    global game_on
    if (
        board[0][0] == "x"
        and board[0][1] == "x"
        and board[0][2] == "x"
        or board[1][0] == "x"
        and board[1][1] == "x"
        and board[1][2] == "x"
        or board[2][0] == "x"
        and board[2][1] == "x"
        and board[2][2] == "x"
        or board[0][0] == 'x'
        and board[0][1] == 'x'
        and board[0][2] == 'x'
        or board[0][1] == 'x'
        and board[1][1] == 'x'
        and board[2][1] == 'x'
        or board[0][2] == 'x'
        and board[1][2] == 'x'
        and board[2][2] == 'x'
        or board[0][0] == 'x'
        and board[1][1] == 'x'
        and board[2][2] == 'x'
        or board[0][2] == 'x'
        and board[1][1] == 'x'
        and board[2][0] == 'x'
    ):
        print("x is winner.")
        game_on = False
        return game_on
    elif(
        board[0][0] == "o"
        and board[0][1] == "o"
        and board[0][2] == "o"
        or board[1][0] == "o"
        and board[1][1] == "o"
        and board[1][2] == "o"
        or board[2][0] == "o"
        and board[2][1] == "o"
        and board[2][2] == "o"
        or board[0][0] == 'o'
        and board[0][1] == 'o'
        and board[0][2] == 'o'
        or board[0][1] == 'o'
        and board[1][1] == 'o'
        and board[2][1] == 'o'
        or board[0][2] == 'o'
        and board[1][2] == 'o'
        and board[2][2] == 'o'
        or board[0][0] == 'o'
        and board[1][1] == 'o'
        and board[2][2] == 'o'
        or board[0][2] == 'o'
        and board[1][1] == 'o'
        and board[2][0] == 'o'
    ):
        print("o is winner.")
        game_on = False
        return game_on
    elif(
        board[0][0] != "-"
        and board[0][1] != "-"
        and board[0][2] != "-"
        and board[1][0] != "-"
        and board[1][1] != "-"
        and board[1][2] != "-"
        and board[2][0] != "-"
        and board[2][1] != "-"
        and board[2][2] != "-"
    ):
        print('cat')
        game_on = False
        return game_on

while game_on:
    if x:
        print("x Turn")
        choice()
        x = False
    else:
        print("o Turn")
        choice()
        x = True
    check_winner()
    print_board()
