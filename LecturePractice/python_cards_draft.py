# Define card suits and ranks
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Loop through all possible cards and print them in a row
for suit in suits:
    for rank in ranks:
        print(f'┌─────────┐ ', end='')
    print('')
    for rank in ranks:
        print(f'|         | ', end='')
    print('')
    for rank in ranks:
        print(f'|    {rank}    | ', end='')
    print('')
    for rank in ranks:
        print(f'|         | ', end='')
    print('')
    for rank in ranks:
        print(f'|    {suit}    | ', end='')
    print('')
    for rank in ranks:
        print(f'|         | ', end='')
    print('')
    for rank in ranks:
        print(f'|         | ', end='')
    print('')
    for rank in ranks:
        print(f'└─────────┘ ', end='')
    print('')
