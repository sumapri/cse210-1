

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = True
turns = 0


def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


def leave(player_input):
    if player_input.lower() == "q":
        print("See you latter.")
        return True
    else:
        return False


def check_input(player_input):
    if not number(player_input):
        return False
    player_input = int(player_input)
    if not boundaries(player_input):
        return False

    return True


def number(player_input):
    if not player_input.isnumeric():
        print("Not a valid number.")
        return False
    else:
        return True


def boundaries(player_input):
    if player_input > 9 or player_input < 1:
        print("Wrong move!")
        return False
    else:
        return True


def taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("Choose another number, this is already taken. ")
        return True
    else:
        return False


def coordinates(player_input):
    row = int(player_input / 3)
    column = player_input
    if column > 2:
        column = int(column % 3)
    return (row, column)


def add_to_board(coords, board, active_player):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_player


def current_player(player):
    if player:
        return "x"
    else:
        return "o"


def winner(player, board):
    if check_row(player, board):
        return True
    if check_column(player, board):
        return True
    if check_diag(player, board):
        return True
    return False


def check_diag(player, board):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def check_column(player, board):
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != player:
                complete_column = False
                break
        if complete_column:
            return True
    return False


def check_row(player, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != player:
                complete_row = False
                break
        if complete_row:
            return True
    return False


while turns < 9:
    active_player = current_player(player)
    print_board(board)
    player_input = input(
        "Let's start. Please choose a number from 1 through 9 or enter \"q\" to leave:")
    if leave(player_input):
        break
    if not check_input(player_input):
        print("Try again.")
        continue
    player_input = int(player_input) - 1
    coords = coordinates(player_input)
    if taken(coords, board):
        print("Try again.")
        continue
    add_to_board(coords, board, active_player)
    if winner(active_player, board):
        print(f"{active_player.upper()}, won the game!")
        break

    turns += 1
    if turns == 9:
        print("No winners, It's a tie!")
    player = not player
