from .card import *
from random import shuffle

class Deck:

    def __init__(self):
        self.ranks = ["Ace", "2", "3", "4", "5", "6", 
                 "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        self.suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

        self.deck = []

        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card(rank,suit))
        
        shuffle(self.deck)
    
    def __repr__(self) -> str:
        return str([repr(x) for x in self.deck])

    def size(self) -> int:
        return len(self.deck)
        
