'''Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc.'''

'''
To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden (1 card face up 1 card face down)
Show both of the Player's cards (2 cards face up)
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

PLAYING = True

class Card:
    '''CARD class for a single card'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        #self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    '''class for a Deck of cards'''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def shuffle_deck(self):
        '''randomly shuffle the deck'''
        random.shuffle(self.deck)
    def deal_one(self):
        '''deal one card from deck'''
        return self.deck.pop()
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The Deck has: " + deck_comp
    
#test_deck = Deck()
#print(test_deck)

class Hand: # for computer dealer or player
    '''class for a hand of cards'''
    def __init__(self):
        self.cards = [] # start with empty list as done in Deck class
        self.value = 0 # start with 0 value
        self.aces = 0 #keep track of no. of aces
    
    def add_card(self,card):
        # from Deck.deal() -> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.aces += 1 

    def adjust_for_ace(self):
        
        # If total value > 21 and I still have an ace
        # Then change my Ace to be a 1 instead of an 11 as in dictionary
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
'''
test_deck = Deck()
test_deck.shuffle_deck()

test_player = Hand()
pulled_card = test_deck.deal_one()
print(pulled_card)
test_player.add_card(pulled_card) Can be coded as: test_player.add_card(test_deck.deal_one())
print(test_player.value)
'''
class Chips:
    def __init__(self, total=100):
        self.total = total # can be default value or user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, the bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have {}". format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please enter h or s only.")
            continue
        break
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <First card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    '''for loop can be written as 
    print("\nPlayer's Hand:", *player.cards, sep='\n ')'''
    
def show_all(player,dealer):
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print(card)
    #calculate and display value J+K == 20
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")
'''show_all function can be written as
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)'''   

'''
list1 = [1,2,3]
print("Items are",*list1, sep = '\n')'''

# end of game scenarios

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# gameplay

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break