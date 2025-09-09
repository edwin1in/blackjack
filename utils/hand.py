from card import *

class Hand:

    def __init__(self):
        self.cards = []
    
    def __repr__(self) -> str:
        return str([repr(x) for x in self.cards])
    
    def append(self, card: Card) -> None:
       self.cards.append(card) 

