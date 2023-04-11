# TicTacToe
# Board
board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
board_position = [1, 3, 5, 9, 11, 13, 17, 19, 21]


def main():
    display_board()
    while True:
        playerX_turn()
        if game_won():
            print("Player X wins!")
            break
        elif draw():
            print("Draw")
            break
        playerO_turn()
        if game_won():
            print("Player O wins!")
            break
        elif draw():
            print("Draw")
            break


# Display board
def display_board():
    print(board)


# Display turns
def playerX_turn():
    global board
    position = input("Player X, choose a position: ")
    if is_valid(position):
        board = board.replace(position, "❌")
        display_board()
    else:
        print("Postion not valid")
        playerX_turn()


def playerO_turn():
    global board
    position = input("Player O, choose a position: ")
    if is_valid(position):
        board = board.replace(position, "⭕")
        display_board()
    else:
        print("Position not valid")
        playerO_turn()


# Check if position is valid
def is_valid(position):
    for i in board_position:
        if position == board[i]:
            return True
    return False


# Game winning condition
#  1  3  5
#  9 11 13
# 17 19 21
def game_won():
    if (
        board[1] == board[3] == board[5]
        or board[9] == board[11] == board[13]
        or board[17] == board[19] == board[21]
        or board[1] == board[9] == board[17]
        or board[3] == board[11] == board[19]
        or board[5] == board[13] == board[21]
        or board[1] == board[11] == board[21]
        or board[5] == board[11] == board[17]
    ):
        return True
    return False


# Game drawing conditions
def draw():
    for i in board_position:
        if board[i] != "X" and board[i] != "O":
            return False
    return True


if __name__ == "__main__":
    main()
