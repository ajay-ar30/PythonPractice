'''
Program for a tic tac toe game for two players on a 3x3 board. Pylint rating 10/10; initial 4.59.
'''

#Set up the tic tac toe board and display it.
import os
import random

def cls():
    '''Clears the screen'''
    os.system('cls' if os.name=='nt' else 'clear')

def display_board(board):
    '''Displays the 3x3 tic tac toe board.'''
    cls()
    for i in range(1, 10, 3):
        print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i != 7:
            print('-----------')

def player_input():
    '''Accepts a player input and assign their marker as 'X' or 'O'.'''
    marker = ''

    # Assign player 1 marker
    while marker not in ['X','O']:
        marker = input('Player 1, choose X or O:').upper()

    # Assign player 2 opposite marker
    if marker == 'X':
        return ('X', 'O')
    return ('O', 'X')

def place_marker(board, marker, position):
    '''Accepts the board list,a marker(X/O),a position(1-9) and assigns it to the board.'''
    board[position] = marker

def check_win(board, mark):
    '''Accepts a board and a mark (X or O) and then checks to see if that mark has won.'''
    # check rows
    for i in range(1, 10, 3):
        if board[i] == board[i+1] == board[i+2] == mark and board[i] != ' ':
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == mark and board[i] != ' ':
            return True
    # check diagonals
    if board[1] == board[5] == board[9] == mark and board[1] != ' ':
        return True
    if board[3] == board[5] == board[7] == mark and board[3] != ' ':
        return True
    return False

def choose_first():
    '''Randomly decides which player goes first.'''
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    return 'Player 2'

def space_check(board, position):
    '''Returns a boolean indicating whether a space on the board is freely available.'''
    return board[position] == ' '

def full_board_check(board):
    '''Checks if the board is full and returns a boolean value. True if full, False otherwise.'''
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, current_player):
    '''Accepts player's next position (1-9),then check if it's a free position.'''
    choice = 0
    while choice not in range(1,10):
        try:
            choice = int(input(f'\n{current_player}, choose your next position: (1-9)'))
            if choice not in range(1,10):
                print("\nInput out of range. Please enter a number between 1 and 9.")
            else:
                if not space_check(board, choice):
                    print(f"\nPosition {choice} is not free on the board")
                    choice = 0 # set choice to 0 to force the player to choose again
                else:
                    break
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
    return choice

def replay():
    '''Asks the player if they want to play again and returns True if they do want to play again.'''
    play_again = input('\nDo you want to play again? Enter yes or no: ')
    return play_again.lower().startswith('y')

#Running the game
print('\nWelcome to Tic Tac Toe!')

while True:
    # Set the game up here (board, who goes first, choose marker - X or O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    TURN = choose_first()
    print('\n'+TURN + ' will go first')

    play_game = input('\nAre you ready to play? Enter Yes or No.')

    GAME_ON = bool(play_game.lower()[0] == 'y') #simplifiable-if-else PEP8 R1703

    while GAME_ON:
        if TURN == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a POSITION
            POSITION = player_choice(the_board,TURN)
            # place the marker on the POSITION of choice
            place_marker(the_board,player1_marker,POSITION)
            # did the player win or is there a tie?
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print("\nPlayer 1 has won!")
                GAME_ON = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nThe game is a draw!")
                    GAME_ON = False
                else:
                    TURN = 'Player 2' # no tie and no win ? Player 2 turn
        else:
            # show the board
            display_board(the_board)
            # choose a POSITION
            POSITION = player_choice(the_board,TURN)
            # place the marker on the POSITION of choice
            place_marker(the_board,player2_marker,POSITION)
            # did the player win or is there a tie?
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print("\nPlayer 2 has won!")
                GAME_ON = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nThe game is a draw!")
                    GAME_ON = False
                else:
                    TURN = 'Player 1'
    if not replay():
        break
