'''
Program for the War card game. Check Wikipedia for more info.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
suit_symbols = {
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣',
    'spades': '♠'
}
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
            '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

#CARD class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self): #useful when using print() function to print instance of class as it looks at what this method returns for the instance
        return self.rank + " of " + self.suit
    '''def print_card(self):
        for rank in ranks:
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
                print()'''
#my_card = Card("Hearts","Two")
#print(my_card.value)

#Deck class
class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
    
#Player class
class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = []

    def remove_one(self): #should happen from top of deck realistically and from start of list in code
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.player_cards.extend(new_cards)
        else:
            # for adding single card object
            self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'
'''
- need to have a shuffled deck of 52 cards
- 26 each need to go to 2 players
- check-loss: does any player have 0 cards? len(card_list) if no -> game_on = True else False
- check drawn cards;whichever player got higher ranking card gets the card of other player and keeps own card too
- check war if both players got same rank cards;players draws additional 3 cards face down -> draw another card
face up & player with higher rank takes all cards->if still war then process repeats till one player loses all cards

'''

#New game
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()
'''for card_object in new_deck.all_cards:
    print(card_object)'''

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#print(len(player_one.player_cards))
#print(len(player_two.player_cards))

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round number {round_num}")
    
    if len(player_one.player_cards) == 0:
        print("Player one has no cards left. Player two wins!")
        game_on = False
        break
    if len(player_two.player_cards) == 0:
        print("Player two has no cards left. Player one wins!")
        game_on = False
        break

    # Start a new round and reset current cards "on the table"

    playerone_playcards = []
    playertwo_playcards = []

    playerone_playcards.append(player_one.remove_one())
    playertwo_playcards.append(player_two.remove_one())

    print(f"Player one: {playerone_playcards[-1].rank} of {playerone_playcards[-1].suit}")
    print(f"Player two: {playertwo_playcards[-1].rank} of {playertwo_playcards[-1].suit}")

    '''playerone_playcards (and playertwo_playcards) are the cards that are played from their respective hands -- 
    in an actual card game, those would be the cards that are put down on the table face-up to see who wins the hand.'''

    '''
    Compare Player cards - 
    playerone_playcards > playertwo_playcards
    playerone_playcards < playertwo_playcards
    playerone_playcards == playertwo_playcards

    at_war = False if players resolve the match-up on the first drawn card, otherwise we will add cards to the current cards on the table. 
    To keep game short, if there is a tie, each player needs to draw 5 additional cards and a player loses if they dont have at least 5 cards to play the war.

    '''
    at_war = True
    while at_war:
        
        if playerone_playcards[-1].value > playertwo_playcards[-1].value:
            player_one.add_cards(playerone_playcards)
            player_one.add_cards(playertwo_playcards)
            at_war = False
            
        elif playerone_playcards[-1].value < playertwo_playcards[-1].value:
            player_two.add_cards(playerone_playcards)
            player_two.add_cards(playertwo_playcards)
            at_war = False
            
        else:
            print("WAR!")
            if len(player_one.player_cards) < 5:
                print("Player one unable to play war. Player two wins!")
                game_on = False
                break

            elif len(player_two.player_cards) < 5:
                print("Player two unable to play war. Player one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    playerone_playcards.append(player_one.remove_one())
                    playertwo_playcards.append(player_two.remove_one())
'''
To modify the War card game for 2 players to be played on 2 computers remotely, 
you would need to implement a network communication protocol to allow the two players to communicate with each other and exchange information about the game. 

Figure out how each player would choose a card from their deck and show it.

Here are some steps you can follow:

Choose a networking protocol: You can choose a protocol like TCP/IP or UDP to create a network connection between the two computers. 
You can use Python's built-in socket library to create sockets and establish a connection between the two computers.

Implement the network communication: You will need to define a communication protocol between the two players that allows them to exchange information about the game. 
This could include sending messages about the cards played, the current state of the game, and so on. You can define a simple protocol using JSON or XML to encode the messages.

Modify the game loop: You will need to modify the game loop to take into account the network communication. 
For example, instead of waiting for player input, you will need to wait for a message from the other player over the network.

Implement error handling: You will need to handle errors that may occur during network communication, such as a player disconnecting or a message being lost.

Test the game: Once you have implemented the network communication and modified the game loop, you can test the game on two separate computers to make sure everything works as expected.

Note that implementing a networked version of the War card game can be quite complex, especially if you have limited experience with networking and Python. 
You may want to start with simpler networking projects to build up your skills before attempting a project like this.

'''

'''
In order to allow two players to choose a card in each round while playing the game remotely, you can use a client-server architecture. 
The server will act as the game host, managing the game state and sending updates to both clients. Each client will connect to the server and interact with it to play the game.

Here's a basic outline of how you could modify the game for remote play:

Modify the code to split it into two parts: a server program and a client program. 
The server will contain the game logic and maintain the game state, while the clients will send player input and receive updates from the server.

The server will listen for incoming connections from clients. When two clients have connected, the server will start the game.

During each round, the server will send the current game state to both clients, including the current face-up card and each player's hand.

Each client will display the current game state and prompt the user to choose a card to play.

The client will send the chosen card to the server, which will update the game state and send the updated state to both clients.

The round will continue until one player wins all the cards or a predetermined number of rounds have been played.

At the end of the game, the server will send the final scores to both clients, and the clients will display them to the user.

Here's a rough example of how you could modify the play_game function to work in a client-server architecture:

def play_game(server_socket):
    # Initialize the game state
    deck = create_deck()
    random.shuffle(deck)
    player1_hand, player2_hand = deal_cards(deck)

    while len(player1_hand) > 0 and len(player2_hand) > 0:
        # Draw the top card from each player's hand
        player1_card = player1_hand.pop(0)
        player2_card = player2_hand.pop(0)

        # Send the current game state to both clients
        game_state = {
            'player1_hand': player1_hand,
            'player2_hand': player2_hand,
            'face_up_card': player2_card,
            'player1_card': None,  # Set to None for now
            'player2_card': None   # Set to None for now
        }
        send_game_state_to_clients(server_socket, game_state)

        # Get the player's chosen card from the client
        player1_card_index = receive_player_card_from_client(server_socket, player1_hand)
        player1_card = player1_hand.pop(player1_card_index)

        # Update the game state with the chosen card and send to clients
        game_state['player1_card'] = player1_card
        send_game_state_to_clients(server_socket, game_state)

        # Repeat for player 2
        player2_card_index = receive_player_card_from_client(server_socket, player2_hand)
        player2_card = player2_hand.pop(player2_card_index)
        game_state['player2_card'] = player2_card
        send_game_state_to_clients(server_socket, game_state)

        # Determine the winner of the round and update the hands accordingly
        winner = determine_round_winner(player1_card, player2_card)
        if winner == 'Player 1':
            player1_hand.extend([player1_card, player2_card])
        else:
            player2_hand.extend([player1_card, player2_card])

    # Determine the winner of the game
    if len(player1_hand) == 0:
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')

    # Send the final scores to both clients
    final_scores = {
        '


'''