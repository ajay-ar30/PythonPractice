# TIC TAC TOE Game
'''Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.'''

import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display_board(board):
    cls()
    for i in range(1, 10, 3):
        print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i != 7:
            print('-----------')

'''Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.'''

def player_input():
    marker = ''

    # Assign player 1 marker
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O:').upper()

    # Assign player 2 opposite marker
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

'''Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.'''
def place_marker(board, marker, position):
    board[position] = marker

'''Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.'''

# Win TIC TAC TOE?

def check_win(board, mark):
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

'''Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.'''

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

'''Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.'''

def space_check(board, position):
    return board[position] == ' ' 
    
'''Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.'''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
  
'''Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.'''

def player_choice(board, current_player):
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

'''Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.'''

def replay():
    play_again = input('\nDo you want to play again? Enter yes or no: ')
    if play_again.lower().startswith('y'):
        return True
    else:
        return False    

'''Step 10: Use while loops and the functions you've made to run the game!'''

print('\nWelcome to Tic Tac Toe!')

while True:
    # Set the game up here (board, who goes first, choose marker - X or O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('\n'+turn + ' will go first')

    play_game = input('\nAre you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board,turn)

            # place the marker on the position of choice
            place_marker(the_board,player1_marker,position)

            # did the player win or is there a tie?
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print("\nPlayer 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nThe game is a draw!")
                    game_on = False
                else:
                    turn = 'Player 2' # no tie and no win ? Player 2 turn
        
        else:
            # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board,turn)

            # place the marker on the position of choice
            place_marker(the_board,player2_marker,position)

            # did the player win or is there a tie?
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print("\nPlayer 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("\nThe game is a draw!")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break