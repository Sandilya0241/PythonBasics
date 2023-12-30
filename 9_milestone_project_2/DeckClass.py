from CardClass import Card, ranks, suits
from random import shuffle

class Deck:
    
    def __init__(self):
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                #CARD OBJECT
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)


    def shuffle_deck(self):
        shuffle(self.all_cards)


    def deal_one(self):
        return self.all_cards.pop() 