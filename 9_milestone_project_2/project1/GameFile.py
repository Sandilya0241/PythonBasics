from CardClass import Card,ranks,suits
from DeckClass import Deck
from PlayerClass import Player 
from time import sleep
from random import randint

AGREED_ADITIONAL_CARDS = 5

if __name__ == "__main__":
    
    # INITIALIZATIONS
    game_on = True
    round_num = 0

    # USER MESSAGES
    print("Welcome to cards game!!")

    # CREATE PLAYERS
    player1 = Player("ONE")
    player2 = Player("TWO")

    # CREATE DECK AND DEAL CARDS TO PLAYERS FROM DECK
    deck = Deck()
    deck.shuffle_deck()
    while len(deck.all_cards) != 0:
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())
    
    # START GAME
    while game_on:

        # START A NEW ROUND
        round_num += 1
        print(f"Round number : {round_num}")

        if len(player1.all_cards) == 0:
            print(f"{player1.name} is out of cards. {player2.name} won the game")
            game_on = False
            break

        if len(player2.all_cards) == 0:
            print(f"{player2.name} is out of cards. {player1.name} won the game")
            game_on = False
            break

        player1_cards_list = []
        player1_cards_list.append(player1.remove_one())
        player2_cards_list = []
        player2_cards_list.append(player2.remove_one())

        # INITIALIZATIONS
        at_war = True

        while at_war:
            if player1_cards_list[-1].value > player2_cards_list[-1].value:
                player1.add_cards(player2_cards_list)
                player1.add_cards(player1_cards_list)
                at_war = False
            elif player1_cards_list[-1].value < player2_cards_list[-1].value:
                player2.add_cards(player1_cards_list)
                player2.add_cards(player2_cards_list)
                at_war = False
            else:
                print("WAR!!!")
                if len(player1.all_cards) < AGREED_ADITIONAL_CARDS:
                    print(f"{player2.name} is out of cards. {player1.name} won the game")
                    game_on = False
                    break
                elif len(player2.all_cards) < AGREED_ADITIONAL_CARDS:
                    print(f"{player1.name} is out of cards. {player2.name} won the game")
                    game_on = False
                    break
                else:
                    for _ in range(AGREED_ADITIONAL_CARDS):
                        player1_cards_list.append(player1.remove_one())
                        player2_cards_list.append(player2.remove_one())
