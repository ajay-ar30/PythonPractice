# TIC TAC TOE Game
'''
1. We need to print a board.
2. Take in player input.
3. Place their input on the board.
4. Check if the game is won,tied, lost, or ongoing.
5. Repeat c and d until the game has been won or tied.
6. Ask if players want to play again.
Break these into smaller sub-problems
'''
# 3x3 matrix construct:

'''for index, item in enumerate('---------', start=1):
    print(item, end=' ' if index % 3 else '\n')

listA=['a','b','c','d','e','f','g','h','i']

for i in range(0, len(listA), 3):
    print ("{} {} {}".format(*listA[i:i+3]))

Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

print('\n'*100) - This scrolls the previous board up out of view. 

Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.'''

import os
import random
#import numpy as np

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def display_board(board):
    cls()
    '''print('Current board is: \n')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')'''
    for i in range(1, 10, 3):
        print(' ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i != 7:
            print('-----------')
    '''for index, item in enumerate(board, start=1):
        print(item, end='-' if index % 3 else '\n')'''

'''TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary'''
#test_board = ['#','O','X','O','X','O','X','O','X','O']
#display_board(test_board)

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
    
'''TEST Step 2: run the function to make sure it returns the desired output'''

#player_input()

'''Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.'''
def place_marker(board, marker, position):
    board[position] = marker
    
'''TEST Step 3: run the place marker function using test parameters and display the modified board'''

#place_marker(test_board,'$',9)
#display_board(test_board)

'''Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.'''

# Win TIC TAC TOE?

#All Rows check if they all share same marker
#All columns check if marker matches
#2 diagonals, check to see match
# 012
# 345
# 678
# You can make a set of each row, and check its length. If it contains only one element, then the game has been won.
'''import numpy as np

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


a = [['X', 'A', 'X'],
     ['A', 'X', 'A'],
     ['A', 'X', 'A']]

print(checkWin(a))
'''
# Below function will return "O" if there is a full line of "O", "X" if there is a line of "X", and 0 otherwise.

'''chatGPT alternative:
'''
def check_win(board, mark):
    # check rows
    for i in range(1, 10, 3):
        if board[i] == board[i+1] == board[i+2] == mark and board[i] != ' ': # 0 == 1 == 2, 3 == 4 == 5, 6 == 7 == 8
            return True
    
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == mark and board[i] != ' ': # 0 == 3 == 6, 1 == 4 == 7, 2 == 5 == 8
            return True
    
    # check diagonals
    if board[1] == board[5] == board[9] == mark and board[1] != ' ':
        return True
    
    if board[3] == board[5] == board[7] == mark and board[3] != ' ':
        return True
    
    return False

'''test_board = ['#','0', 'A', 'X', 
                  'A', 'X', 'O',
                  'X', '0', 'X']'''

'''TEST Step 4: run the win_check function against our test_board - it should return True'''

#check_win(test_board,'X')

'''Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.'''

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
current_player = choose_first()    

'''Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.'''

def space_check(board, position):
    return board[position] == ' '
'''Can be written as:
if board[position] == '':
        return True
    else:
        return False''' 
    
'''Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.'''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
  
'''Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
test_board = ['#','X', 'A', 'X', 
                  'A', 'X', 'O',
                  'X', 'X', '']''' # made test board of 10 items so user can select numbers 1 - 9 to enter

def player_choice(board): 
    choice = 0
    '''while choice not in range(1,10) or not space_check(board, choice):
        choice = int(input('Choose your next position: (1-9) '))
    return choice'''
    while choice not in range(1,10) or not space_check(board, choice):
        try:
            choice = int(input(f'{current_player} choose your next position: (1-9)'))
            if choice not in range(1,10) or not space_check(board, choice):
                print(choice, "\n")
                print("Input out of range. Please enter a number between 1 and 9.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")   
    if space_check(board, choice):
        return choice
    return 'Position not free on board' #need to figure out how to reach this code    

'''Escape key press
keyboard.is_pressed('esc'):
                print("Escape key pressed. Exiting program.")
                sys.exit()'''

#player_choice(test_board)
'''Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.'''

def replay():
    play_again = input('Do you want to play again? Enter yes or no: ')
    if play_again.lower().startswith('y'):
        return True
    else:
        return False
#replay()    

'''Step 10: Use while loops and the functions you've made to run the game!'''

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here (board, who goes first, choose marker - X or O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker on the position of choice
            place_marker(the_board,player1_marker,position)

            # did the player won or if there is a tie?
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    game_on = False
                else:
                    turn = 'Player 2'
        # no tie and no win ? Player 2 turn
        else:
            # show the board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker on the position of choice
            place_marker(the_board,player2_marker,position)

            # did the player won or if there is a tie?
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
