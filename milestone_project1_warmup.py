# Warmup:
# User input validation -

def user_choice():
    
    choice ='WRONG'
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
    
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False
    return int(choice)
user_choice()

'''Simple User Interaction

Finally let's combine all of these ideas to create a small game where a user can choose a "position" in an existing list and replace it with a value of their choice.

1. print game list
2. user chooses index position to replace item
3. replaces item at position and print current list
4. continue playing game or no

'''
game_list = [0,1,2]

def display_game(game_list):
    print('Here is the current list:')
    print(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input('Select a position (0, 1 or 2):')
        if choice not in ['0','1','2']:
            print('Sorry! Invalid choice')
    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input('Type a string to place at position')
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('Keep playing? (Y or N)')
        if choice not in ['Y','N']:
            print('Invalid choice. Please choose Y or N')
    if choice == 'Y':
        return True
    else:
        return False

# GameLogic - 

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()


test_board = ['-','-','-','-','-','-','-','-','-']
if len(set([test_board[i][i] for i in range(0,len(test_board)-1)])) == 1:
    print(test_board[0][0])
elif len(set([test_board[i][len(test_board)-i-1] for i in range(0,len(test_board)-1)])) == 1:
    print(test_board[0][len(test_board)-1])
else:
    pass
