# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 2
suits = ["♣️","♦️","❤️","♠️"]
ranks = [None, "A"] + [str(x) for x in range(2,11)]  + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 9
class Card:
    """
    A standard playing card.
    """
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __repr__(self):
        return ranks[self.rank] + suits[self.suit]
    
    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)
