from CardClass import Card,ranks,suits
from DeckClass import Deck
from PlayerClass import Player 
from time import sleep
from random import randint

AGREED_ADITIONAL_CARDS = 5

def player_selection(players):
    
    ##
    #
    # This method will randomly select between Players randInt(). This is like a toss.
    #
    ##

    print("Tossing the coin\n")
    print("..........")
    sleep(3)
    toss_won = players[randint(0,len(players)-1)]
    print(f"\n{toss_won} will play first\n")
    return toss_won

if __name__ == "__main__":
    print("Welcome to cards game!!")
    
    # Create players
    print("Creating player profiles before games...")
    player1 = Player(input("Please provide player1 name:"))
    player2 = Player(input("Please provide player2 name:"))

    # Select a player to start the game.
    turn = player_selection([player1.name,player2.name])
    
    # Deal cards to players from deck
    deck = Deck()
    deck.shuffle_deck()
    while len(deck.all_cards) != 0:
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())
            
    game_on = True
    round_num = 0
    at_war = False

    while game_on:
        if len(player1.all_cards) == 0 or len(player2.all_cards) == 0:
            game_on = False
            if len(player1.all_cards) == 0:
                print(f"{player1.name} is out of cards. {player2.name} won the game")
            else:
                print(f"{player2.name} is out of cards. {player1.name} won the game")
        else:
            # Start a new round
            round_num += 1
            print(f"Round number : {round_num}")
            
            player1_cards_list = []
            player1_cards_list.append(player1.remove_one())
            player2_cards_list = []
            player2_cards_list.append(player2.remove_one())

            if player1_cards_list[-1] == player2_cards_list[-1]:
                at_war = True
                while at_war:
                    if player1_cards_list[-1] > player2_cards_list[-1]:
                        player1.add_cards(player2_cards_list)
                        player1.add_cards(player1_cards_list)
                        at_war = False
                    elif player1_cards_list[-1] > player2_cards_list[-1]:
                        player2.add_cards(player1_cards_list)
                        player2.add_cards(player2_cards_list)
                        at_war = False
                    else:
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
            else:
                if player1_cards_list[-1] > player2_cards_list[-1]:
                    player1.add_cards(player2_cards_list)
                    player1.add_cards(player1_cards_list)
                else:
                    player2.add_cards(player1_cards_list)
                    player2.add_cards(player2_cards_list)