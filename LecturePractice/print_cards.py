# Define the card suit symbols
suit_symbols = {
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣',
    'spades': '♠'
}

# Define the card ranks
card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Define the card width and height in characters
card_width = 11
card_height = 7

# Loop over each rank and suit to create a card
for rank in card_ranks:
    for suit in suit_symbols.values():
        # Print the top of the card
        print('┌─────────┐')
        
        # Print the card rank and suit symbol
        print(f'│ {rank:<2}      │')
        print('│         │')
        print(f'│    {suit}    │')
        print('│         │')
        print(f'│      {rank:>2} │')
        
        # Print the bottom of the card
        print('└─────────┘')
        
        # Add a space between each card
        print()

#This code prints each card as a separate block with a rank and a suit symbol. You can modify the ASCII characters used to create the card to fit your preferences.

'''---------------------Visually printing a deck of available cards-----------------------------------'''
'''# Define the card suit symbols
suit_symbols = {
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣',
    'spades': '♠'
}

# Define the card ranks
card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Define the card width and height in characters
card_width = 11
card_height = 7

# Define the number of cards available
num_cards = 10

# Define the height of the card stack
stack_height = card_height * num_cards

# Loop over each rank and suit to create a card
for rank in card_ranks:
    for suit in suit_symbols.values():
        # Print the top of the card stack
        print(' ' * (card_width // 2) + '┌─────────┐')
        
        # Loop over the number of cards available to print the card rank and suit symbol
        for i in range(num_cards):
            print(f' ' * (card_width // 2) + f'│ {rank:<2}      │')
            print(' ' * (card_width // 2) + '│         │')
            print(f' ' * (card_width // 2) + f'│    {suit}    │')
            print(' ' * (card_width // 2) + '│         │')
            print(f' ' * (card_width // 2) + f'│      {rank:>2} │')
        
        # Print the bottom of the card stack
        print(' ' * (card_width // 2) + '└─────────┘')
        
        # Add a space between each card
        print()

# Print the full stack of cards
print('\n' * (stack_height - card_height * 4))

In this example, you can change the value of num_cards to adjust the number of cards in the stack. 
The code first calculates the stack_height based on the number of cards, and then prints each card within the stack using nested for loops. 
The final print statement adds additional newlines to ensure that the full stack of cards is displayed.'''


