# game status
board = ["-" for x in range(1, 10)]
winner = None
game_running = True
current_player = "odd"
odd_nums = [x for x in range(1, 10) if x % 2 != 0]
even_nums = [x for x in range(1, 10) if x % 2 == 0]

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def display_game_status():
    global winner, game_running, current_player
    print(f"game_running: {game_running}\ncurrent_player: {current_player}\nWinner: {winner}")
    display_board(board)




# first player
def first_player():
    global board, odd_nums, current_player
    current_player = "odd"
    # choose odd value from 1 to 9
    value = int(input(f"player_odd, choose from {odd_nums} to insert: "))
    odd_nums.remove(value)

    # where to place on the board
    place_on_board = int(input("choose 1-9: ")) - 1
    # check if the value in is odd and in 1-9, check whether the place is empty or not
    if (value in [x for x in range(1, 10) if x % 2 != 0]) and (board[place_on_board] == "-"):
        board[place_on_board] = str(value) # if true then place it on the place
    else:
        print("sorry, place is already taken!!".upper())


# second player
def second_player():
    global board, even_nums, current_player
    current_player = "even"
    value = int(input(f"player_even, choose from {even_nums} to insert: "))
    even_nums.remove(value)
    place_on_board = int(input("choose, 1-9: ")) - 1 # as index starts from 0
    # check if the value in is odd and in 1-9, check whether the place is empty or not
    if (value in [x for x in range(1, 10) if x % 2 == 0]) and (board[place_on_board]) == "-":
        board[place_on_board] = str(value) # there is  a warning as python expected to insert a str not int

    # if not, then the place is already taken
    else:
        print("sorry, place is already taken!!".upper())

##check wins
def check_horizontally():
    global board, current_player
    hwinner = current_player
    if ("-" not in [board[0], board[1], board[2]]) and ((int(board[0]) + int(board[1]) + int(board[2]) == 15)):
        print(f"!!!!!!!!!!!!{hwinner} wins!!!!!!!!!!!!!!".upper())

        return True
    elif ("-" not in [board[3], board[4], board[5]]) and ((int(board[3]) + int(board[4]) + int(board[5]) == 15)):
        print(f"!!!!!!!!!!!!{hwinner} wins!!!!!!!!!!!!!!".upper())

        return True

    elif ("-" not in [board[6], board[7], board[8]]) and ((int(board[6]) + int(board[7]) + int(board[8]) == 15)):
        print(f"!!!!!!!!!!!!{hwinner} wins!!!!!!!!!!!!!!".upper())

        return True


def check_vertically():
    global board, current_player
    vwinner = current_player

    if ("-" not in [board[0], board[3], board[6]]) and ((int(board[0]) + int(board[3]) + int(board[6]) == 15)):
        print(f"!!!!!!!!!!!!{vwinner} wins!!!!!!!!!!!!!!".upper())

    elif ("-" not in [board[1], board[4], board[7]]) and ((int(board[1]) + int(board[4]) + int(board[7]) == 15)):
        print(f"!!!!!!!!!!!!{vwinner} wins!!!!!!!!!!!!!!".upper())

        return True
    elif ("-" not in [board[2], board[5], board[8]]) and ((int(board[2]) + int(board[5]) + int(board[8]) == 15)):
        print(f"!!!!!!!!!!!!{vwinner} wins!!!!!!!!!!!!!!".upper())

        return True


def check_diagonally():
    global board, current_player
    dwinner = current_player

    if ("-" not in [board[2], board[4], board[6]]) and ((int(board[2]) + int(board[4]) + int(board[6]) == 15)):
        print(f"!!!!!!!!!!!!{dwinner} wins!!!!!!!!!!!!!!".upper())

        return True
    if ("-" not in [board[0], board[4], board[8]]) and ((int(board[0]) + int(board[4]) + int(board[8]) == 15)):
        print(f"!!!!!!!!!!!!{dwinner} wins!!!!!!!!!!!!!!".upper())
        return True

def check_win():
    global game_running, winner, current_player
    if check_horizontally() or check_vertically() or check_diagonally():
        winner = current_player
        game_running = False
        quit()



#####check tie
def tie():
    global board
    if "-" not in board:
        print("!!!it's a tie!!!".upper())
        return True
def check_tie():
    global game_running
    if tie():
        input("press enter to exit!!! ".title())
        game_running = False
        quit()





# trail
first_game = True
while game_running:
    if first_game:
        current_player = None
        display_game_status()
        print(f"#########################################################################")
        first_game = False


    first_player()
    display_game_status()
    check_win()
    check_tie()
    print(f"#########################################################################")
    second_player()
    display_game_status()
    check_win()
    check_tie()
    print(f"#########################################################################")














