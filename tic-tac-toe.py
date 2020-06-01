# # (1, 3) (2, 3) (3, 3)
# # (1, 2) (2, 2) (3, 2)
# # (1, 1) (2, 1) (3, 1)
# game board
state = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
print(state)

# check for game is over or not
game_is_running = True

# find out who is winner
winner = None

# who is current player(X is always first)
current_player = "X"


# game of tic tac toe
def play_game():
    # show game state
    board_state()

    # loop until game is win or tie
    while game_is_running:

        # handle turn
        handle_turn(current_player)

        # check game is over
        check_game()

        # flip to other player
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " wins")
    elif winner == None:
        print("Draw")

# display game board state


def board_state():
    print("-" * 9)
    print(f"| {state[0]} {state[1]} {state[2]} |")
    print(f"| {state[3]} {state[4]} {state[5]} |")
    print(f"| {state[6]} {state[7]} {state[8]} |")
    print("-" * 9)

# handle a turn for player


def handle_turn(player):
    # coordinates
    table = [[1, 3], [2, 3], [3, 3], [1, 2], [
        2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]

    # get coordinate from player
    print(player + " s turn")
    try:
        # check user input is valid and spot is empty
        coordinate = input().split()
        if coordinate[0].isdigit() and coordinate[1].isdigit():
            if (int(coordinate[0]) >= 1 and int(coordinate[0]) <= 3) and (int(coordinate[1]) >= 1 and int(coordinate[1]) <= 3):
                int_coordinate = [int(coordinate[0]), int(coordinate[1])]

                for i in range(9):
                    if int_coordinate == table[i]:
                        if state[i] == " ":
                            state[i] = player
                        else:
                            print("This cell is occupied! Choose another one!")
                            handle_turn(player)
            else:
                print("Coordinate should be from 1 to 3!")
                handle_turn(player)
        else:
            print("You should enter numbers!")
            handle_turn(player)
    except ValueError:
        print("You should enter numbers!")

    # updated board
    board_state()

# check game is over or not


def check_game():
    check_winner()
    check_tie()

# check who is winner


def check_winner():
    # set globle variable
    global winner
    # check winner possibility
    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    # get winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# check the rows for winner


def check_rows():
    # set global variable
    global game_is_running
    # check row has same value
    row_1 = state[0] == state[1] == state[2] != " "
    row_2 = state[3] == state[4] == state[5] != " "
    row_3 = state[6] == state[7] == state[8] != " "
    # if any row have match flag that win
    if row_1 or row_2 or row_3:
        game_is_running = False
    # return winner which is "X" or "O"
    if row_1:
        return state[0]
    elif row_2:
        return state[3]
    elif row_3:
        return state[6]
    else:
        # if no winner
        return None

# check the columns for winner


def check_column():
    # set global variable
    global game_is_running
    # check row has same value
    column_1 = state[0] == state[3] == state[6] != " "
    column_2 = state[1] == state[4] == state[7] != " "
    column_3 = state[2] == state[5] == state[8] != " "
    # if any row have match flag that win
    if column_1 or column_2 or column_3:
        game_is_running = False
    # return winner which is "X" or "O"
    if column_1:
        return state[0]
    elif column_2:
        return state[1]
    elif column_3:
        return state[2]
    else:
        # if no winner
        return None

# check for diagonal for winner


def check_diagonal():
    # set global variable
    global game_is_running
    # check row has same value
    diagonal_1 = state[0] == state[4] == state[8] != " "
    diagonal_2 = state[2] == state[4] == state[6] != " "

    # if any row have match flag that win
    if diagonal_1 or diagonal_2:
        game_is_running = False
    # return winner which is "X" or "O"
    if diagonal_1:
        return state[0]
    elif diagonal_2:
        return state[2]
    else:
        # if no winner
        return None

# check it there is a tie


def check_tie():
    # set global variable
    global game_is_running
    # if board is full
    if " " not in state:
        game_is_running = False
        return True
    # else no tie
    else:
        return False

# flip current player X to O or O to X


def flip_player():
    # global variable we need
    global current_player
    # if current player was X , make it O
    if current_player == "X":
        current_player = "O"
        # else make "X"
    elif current_player == "O":
        current_player = "X"


# start game
play_game()
