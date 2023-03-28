from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        display_board(board)
        free_fields, _ = make_list_of_free_fields(board)
        move = input("Enter your move: ")
        if not move.isdigit():
            print("Invalid input. Move must be an integer number!")
            continue
        move = int(move)
        if not 1 <= move <= 9:
            print("Invalid input. Move must be between 1 and 9!")
            continue
        row, col = [
            (i, j)
            for i, row in enumerate(board)
            for j, val in enumerate(row)
            if val == move
        ][0]
        if (row, col) not in free_fields:
            print("Move cannot point to a field which is already occupied!")
            continue
        board[row][col] = "O"
        victory = victory_for(board, "O")
        if victory:
            display_board(board)
            print(victory)
            break
        draw_move(board)
        display_board(board)
        victory = victory_for(board, "X")
        if victory:
            print(victory)
            break


def make_list_of_free_fields(board):
    free_board_elemnts = list(range(1, 10))
    free_square_fields = [
        (row, col)
        for row in range(len(board))
        for col in range(len(board[row]))
        if board[row][col] in free_board_elemnts
    ]
    return free_square_fields, free_board_elemnts


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    def win_message(sign):
        if sign == "O":
            return "You won"
        return "Computer won"

    # Check for horizontal, vertical, and diagonal wins
    for i in range(3):
        if (
            board[i][0] == board[i][1] == board[i][2] == sign
            or board[0][i] == board[1][i] == board[2][i] == sign
            or board[0][0] == board[1][1] == board[2][2] == sign
            or board[0][2] == board[1][1] == board[2][0] == sign
        ):
            return win_message(sign)

    # Check for draw
    free_fields, _ = make_list_of_free_fields(board)
    draw_board = [row[:] for row in board]
    for row in range(3):
        for col in range(3):
            if (row, col) in free_fields:
                draw_board[row][col] = ""
    if all([all(row) for row in draw_board]):
        return "Draw"

    # If no win or draw, game is not over
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields, _ = make_list_of_free_fields(board)
    empty_fields_no = len(free_fields)
    computer_move = free_fields[randrange(empty_fields_no)]
    row, col = computer_move
    board[row][col] = "X"


if __name__ == "__main__":
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board[1][1] = "X"
    enter_move(board)
