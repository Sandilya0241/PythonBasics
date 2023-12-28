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
            print("Sorry, that's not a digit")
            continue
        else:
            if not int(choice) in range(1,10):
                print("Sorry, out of range")
                continue 
            elif validate_user_pos_input(choice):
                print("Sorry, that position is already selected by user")
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


if __name__ == "__main__":
    
    game_on = False

    while True:
        playerXO = input(f"\nDecide who want to play as 'PlayerX' and who is 'PlayerO'.\nAfter selecting press 'Y' : ")
        if playerXO == 'Y':
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
            print(turn + " staring the game")
        else:
            print(turn + " staring the game")
        break