from random import randint
from time import sleep
import os


game_board = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
player_sign = {"PlayerX":"X","PlayerO":"O"}


def display_board(clear_board=False):

    ##
    #
    # This method display current board and board after clearing
    #
    ##

    if (clear_board):
        game_board["1"] = " "
        game_board["2"] = " "
        game_board["3"] = " "
        game_board["4"] = " "
        game_board["5"] = " "
        game_board["6"] = " "
        game_board["7"] = " "
        game_board["8"] = " "
        game_board["9"] = " "
    else:
        print()
        print()
        print(f' {game_board["1"]} | {game_board["2"]} | {game_board["3"]} \n---|---|---\n {game_board["4"]} | {game_board["5"]} | {game_board["6"]} \n---|---|--- \n {game_board["7"]} | {game_board["8"]} | {game_board["9"]} ')
        print()
        print()


def user_position_choice():

    ##
    #
    # This method will capture user's choice position
    #
    ##

    choice = -1
    while True:
        choice = input("Please enter a number between 1 to 9 : ")
        if not choice.isdigit():
            print("\nSorry, that's not a digit")
            continue
        else:
            if not int(choice) in range(1,10):
                print("\nSorry, out of range")
                continue 
            elif validate_user_pos_input(choice):
                print("\nSorry, that position was already selected. Please try again!")
                continue
            else:
                break
    return choice


def validate_user_pos_input(pos):
    
    ##
    #
    # This method will validate whether user selected a valid position or not.
    #
    ##

    return game_board[pos] == "X" or game_board[pos] == "O" 


def player_selection():
    
    ##
    #
    # This method will randomly select between PlayerX or PlayerO using randInt(). This is like a toss.
    #
    ##

    players = ["PlayerX","PlayerO"]
    print("Tossing the coin\n")
    print("..........")
    sleep(3)
    toss_won = players[randint(0,len(players)-1)]
    print(f"\n{toss_won} will play first\n")
    return toss_won


def mark_user_selection(mark, pos):
    
    ##
    #
    # This method marks either 'X' or 'O' in position user provided.
    #
    ##

    game_board[pos] = mark


def print_congrats_message(winner):
    
    ##
    #
    # This method just prints Congrats and Player Name
    #
    ##

    print()
    print(" @@@@@  @@@@@  @    @  @@@@@  @@@@@  @@@@@   @@@@@@  @@@@@")
    print(" @      @   @  @ @  @  @      @   @  @   @     @     @    ")
    print(" @      @   @  @  @ @  @ @@@  @@@@@  @@@@@     @     @@@@@")
    print(" @      @   @  @   @@  @   @  @  @   @   @     @         @")
    print(" @@@@@  @@@@@  @    @  @@@@@  @   @  @   @     @     @@@@@")
    print()
    
    if winner == "PlayerX":
        print(" @@@@  @      @@@@@  @   @  @@@@@  @@@@@  @   @")
        print(" @  @  @      @   @   @ @   @      @   @   @ @ ")
        print(" @@@@  @      @@@@@    @    @@@@   @@@@@    @  ")
        print(" @     @      @   @    @    @      @  @    @ @ ")
        print(" @     @@@@@  @   @    @    @@@@@  @   @  @   @")
    else:
        print(" @@@@  @      @@@@@  @   @  @@@@@  @@@@@  @@@@@")
        print(" @  @  @      @   @   @ @   @      @   @  @   @")
        print(" @@@@  @      @@@@@    @    @@@@   @@@@@  @   @")
        print(" @     @      @   @    @    @      @  @   @   @")
        print(" @     @@@@@  @   @    @    @@@@@  @   @  @@@@@")
    
    print()


def check_for_winner(player):
    
    ##
    #
    # This method checks whether player won or not. If won, prints congrats message. 
    #
    ##

    if ((game_board["1"] == game_board["2"] == game_board["3"] == player_sign[player]) or 
        (game_board["4"] == game_board["5"] == game_board["6"] == player_sign[player]) or
        (game_board["7"] == game_board["8"] == game_board["9"] == player_sign[player]) or
        (game_board["1"] == game_board["4"] == game_board["7"] == player_sign[player]) or 
        (game_board["2"] == game_board["5"] == game_board["8"] == player_sign[player]) or
        (game_board["3"] == game_board["6"] == game_board["9"] == player_sign[player]) or
        (game_board["1"] == game_board["5"] == game_board["9"] == player_sign[player]) or 
        (game_board["3"] == game_board["5"] == game_board["7"] == player_sign[player])
        ):
        print_congrats_message(player)
        return True
    return False


def full_board_check():
    
    ##
    #
    # This method checks whether board is full or not.
    #
    ##

    for val in game_board.values():
        if val == " ":
            return False

    return True 


def restart_game():
    
    ##
    #
    # This method enquires with user whether or not to restart the game.
    #
    ##

    while True:
        start_game_again = input(f"\nWould like to play the game again? Please input y to start game again or n to quit: ")
        if start_game_again == 'y':
            os.system('cls')
            return True
        elif start_game_again == 'n':
            os.system('cls')
            return False
        else:
            print("\nInvalid input. Please try again")
            continue

 
if __name__ == "__main__":    
    
    ##
    #
    # Main method
    #
    ##
    
    while True:
        print(" @@@@@@  @@@@@  @@@@@  @@@@@@  @@@@@  @@@@@  @@@@@@  @@@@@  @@@@@")
        print("   @       @    @        @     @   @  @        @     @   @  @    ")
        print("   @       @    @        @     @@@@@  @        @     @   @  @@@  ")
        print("   @       @    @        @     @   @  @        @     @   @  @    ")
        print("   @     @@@@@  @@@@@    @     @   @  @@@@@    @     @@@@@  @@@@@")  
        game_on = False
        display_board(clear_board=True)
        while True:
            playerXO = input(f"\nDecide who wants to play as 'PlayerX' and who wants to play as 'PlayerO'.\nAfter selecting press 'y' : ")
            if playerXO == 'y':
                break
            else:
                print("\nInvalid input. Please try again")
                continue

        print('\nLet us flip a coin to decide who is going to start the game\n')

        turn = player_selection()

        while True:
            play_game = input("\nDo you want to start the game? Enter y to start the game or n to exit:")
            if play_game == 'y':
                game_on = True
                break
            elif play_game == 'n':
                game_on = False
                break
            else:
                print("\nInvalid input. Please try again")
                continue
        
        while game_on:
            
            if turn == "PlayerX":
                print("\nIt's PlayerX turn")
                display_board()
                choosen_pos = user_position_choice()
                mark_user_selection(player_sign[turn],choosen_pos)
                if check_for_winner(turn):
                    game_on = False
                else:
                    if full_board_check():
                        display_board()
                        print("\n\nGame is  tied")
                        break
                    else:
                        turn = "PlayerO"
                
            else:
                print("\nIt's PlayerO turn")
                display_board()
                choosen_pos = user_position_choice()
                mark_user_selection(player_sign[turn],choosen_pos)
                if check_for_winner(turn):
                    game_on = False
                else:
                    if full_board_check():
                        display_board()
                        print("\n\nGame is  tied")
                        break
                    else:
                        turn = "PlayerX"

        display_board()

        if not restart_game():
            break