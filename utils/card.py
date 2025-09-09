class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f'(rank={self.rank},suit={self.suit})'

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'

    def get_rank(self) -> str:
        return self.rank

    def get_suit(self) -> str:
        return self.suit
