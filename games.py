#################################################
# This file creates a menu and runs all the games
# Written by Dan Sulak
#
#################################################

import war, hangman, pick_a_number, rock_paper_scissors

print("Get ready for some fun!!\n\n")

games = True

while games == True:
    which_game = ("1. Hangman \n2. Pick a number \n3. Rock, Paper, Scissors \n4. War\n\nEnter the number of the game you want to play, 'q' to quit:  \n")
    select = input(which_game)

    if select == 'q':
        break

    elif select == '1':
        hangman.hangman()

    elif select == '2':
        pick_a_number.play_pick_a_number()

    elif select == "3":
        rock_paper_scissors.play_r_p_s()

    elif select == '4':
        game = war.Game()
        game.play_game()

    else:
        print("That is not a valid input!\n")
