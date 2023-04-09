'''
Program for the War card game. Check Wikipedia for more info.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#CARD class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self): #useful when using print() function to print instance of class as it looks at what this method returns for the instance
        return self.rank + " of " + self.suit
my_card = Card("Hearts","Two")
print(my_card.value)

#Deck class
class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()
new_deck.shuffle_deck()
for card_object in new_deck.all_cards:
    print(card_object)

deal_card = new_deck.deal_one()
print(deal_card)
print(len(new_deck.all_cards))

class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = []

    def remove_card(self): #should happen from top of deck realistically and from start of list in code
        self.player_cards.pop(0)
        pass

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.player_cards.extend(new_cards)
        else:
            # for adding single card object
            self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'
    
player_one = Player("One")
player_two = Player("Two")
player_one.add_cards([my_card,my_card,my_card])
print(player_one)
player_one.remove_card()
print(player_one)


'''
- need to have a shuffled deck of 52 cards
- 26 each need to go to 2 players
- check-win: does any player have 0 cards? len(card_list)
- 
'''