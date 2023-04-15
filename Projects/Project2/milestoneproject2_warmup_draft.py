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
