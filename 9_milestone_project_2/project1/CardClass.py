import random

suits = ("Spades","Clubs","Hearts","Diamonds")
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
card_values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self):
        return f"{"-" * (len(self.rank + " of " + self.suit) + 2)}\n|{self.rank} of {self.suit}|\n{"-" * (len(self.rank + " of " + self.suit) + 2)}"
