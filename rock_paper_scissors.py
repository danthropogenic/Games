# practicepython.org exercise 8: rock paper scissors

#if __name__ == "__main__":

import random
def play_r_p_s():
     print("Welcome to Rock Paper Scissors!!")
     players = int(input("\n1 or 2 players?  "))
     while players != 1 and players != 2:
          players = input("That's not a valid option. 1 or 2 players?")
     options = ['rock','paper','scissors']
     play = True
     while play:
         print("\nEnter q to quit.\n")
         p1 = input("Player 1: rock, paper, or scissors?  ")
         if p1 == 'q':
             break
         while p1 not in options:
             p1 = input("That's not an option! rock, paper, or scissors?  ")
         print('\n' *80)
         if players == 2:
             p2 = input("Player 2: rock, paper, or scissors?  ")
             p2_name = "player 2"
             p1_name = "Player 1"
             vic = "wins"
         else:
             p2 = options[random.randint(0,2)]
             p2_name = "the computer"
             p1_name = "You"
             vic = "win"
         if p2 == 'q':
             break
         while p2 not in options:
             p2 = input("That's not an option! rock, paper, or scissors?  ")
         print('\n' *80)
         if (p1 == 'rock' and p2 == 'scissors'
             or p1 == 'scissors' and p2 == 'paper'
             or p1 == 'paper' and p2 == 'rock'):
             print("{} chose {} and {} chose {}. {} {}!!".format(p1_name,p1,p2_name,p2,p1_name,vic))
         elif p1 == p2:
             print("You both picked {}. It's a tie".format(p1))
         else:
             print("{} chose {} and {} chose {}. {} wins!!".format(p1_name,p1,p2_name,p2,p2_name))
         again = input("Play again? (y/n)  ")
         while again != 'y' and again != 'n':
             again = input("Play again? (y/n)  ")
         if again == 'n':
             play = False
        
