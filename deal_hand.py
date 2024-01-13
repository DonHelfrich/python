import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_str = str(self.rank)
        if self.rank == 11:
            rank_str = "J"
        elif self.rank == 12:
            rank_str = "Q"
        elif self.rank == 13:
            rank_str = "K"
        return f"{rank_str} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for rank in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("No more cards in the deck.")

class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        for card in self.hand:
            print(card)

def deal_hand():
    # Initialize deck and players
    deck = Deck()
    deck.shuffle()
    hand = Hand("Hand")

    for _ in range(5):
        hand.add_card(deck.deal())

    print("Five card hand:")
    hand.show_hand()

deal_hand()