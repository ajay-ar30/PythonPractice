'''
Program for the War card game. Check Wikipedia for more info.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

class Card:
    '''CARD class for a single card'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    '''class for a Deck of cards'''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle_deck(self):
        '''randomly shuffle the deck'''
        random.shuffle(self.all_cards)
    def deal_one(self):
        '''deal one card from deck'''
        return self.all_cards.pop()

class Player:
    '''class for a player'''
    def __init__(self,name):
        self.name = name
        self.player_cards = []

    def remove_one(self):
        '''remove one card from player deck'''
        return self.player_cards.pop(0)

    def add_cards(self,new_cards):
        '''add cards to player deck'''
        if isinstance(new_cards,list):
            # list of multiple card objects
            self.player_cards.extend(new_cards)
        else:
            # for adding single card object
            self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'

#New game
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#print(len(player_one.player_cards))
#print(len(player_two.player_cards))

GAME_ON = True

ROUND_NUM = 0
while GAME_ON:
    ROUND_NUM += 1
    print(f"Round number {ROUND_NUM}")

    if len(player_one.player_cards) == 0:
        print("Player one has no cards left. Player two wins!")
        GAME_ON = False
        break
    if len(player_two.player_cards) == 0:
        print("Player two has no cards left. Player one wins!")
        GAME_ON = False
        break

    # Start a new round and reset current cards "on the table"

    playerone_playcards = []
    playertwo_playcards = []

    playerone_playcards.append(player_one.remove_one())
    playertwo_playcards.append(player_two.remove_one())

    print(f"Player one: {playerone_playcards[-1].rank} of {playerone_playcards[-1].suit}")
    print(f"Player two: {playertwo_playcards[-1].rank} of {playertwo_playcards[-1].suit}")

    AT_WAR = True
    while AT_WAR:
        if playerone_playcards[-1].value > playertwo_playcards[-1].value:
            player_one.add_cards(playerone_playcards)
            player_one.add_cards(playertwo_playcards)
            AT_WAR = False

        elif playerone_playcards[-1].value < playertwo_playcards[-1].value:
            player_two.add_cards(playerone_playcards)
            player_two.add_cards(playertwo_playcards)
            AT_WAR = False

        else:
            print("WAR!")
            if len(player_one.player_cards) < 5:
                print("Player one unable to play war. Player two wins!")
                GAME_ON = False
                break
            if len(player_two.player_cards) < 5:
                print("Player two unable to play war. Player one wins!")
                GAME_ON = False
                break
            for num in range(5):
                playerone_playcards.append(player_one.remove_one())
                playertwo_playcards.append(player_two.remove_one())
