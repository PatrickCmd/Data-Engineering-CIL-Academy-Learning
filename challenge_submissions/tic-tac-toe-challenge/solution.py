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
        try:
            move = int(input("Enter your move: "))
            response = ""
            if move <= 0 and move >= 10:
                response = (
                    "the number must be valid, i.e. it must be greater "
                    "than `0` and less than `10`"
                )
                print(response)
                continue

            counter = 1
            assigned = False
            victory = None
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if counter == move and (row, col) not in free_fields:
                        response = (
                            "Move cannot point to a field which is already occupied;"
                        )
                        print(response)
                        assigned = True
                        break
                    elif counter == move and (row, col) in free_fields:
                        board[row][col] = "O"
                        victory = victory_for(board, "O")
                        if victory:
                            display_board(board)
                            break
                        assigned = True

                        draw_move(board)
                        display_board(board)
                        victory = victory_for(board, "X")
                        if victory:
                            break
                        break
                    counter += 1
                if assigned or victory is not None:
                    break
            if victory:
                print(victory)
                break

        except ValueError:
            print("Invalid input. Move must be an integer number!")
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_board_elemnts = list(range(1, 10))
    free_square_fields = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in free_board_elemnts:
                free_square_fields.append((row, col))

    return free_square_fields, free_board_elemnts


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    def win_message(sign):
        if sign == "O":
            return "You won"
        return "Computer won"

    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] and row[0] == sign:
            return win_message(sign)

    # Check for vertical wins
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == sign:
            return win_message(sign)

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == sign:
        return win_message(sign)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == sign:
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
