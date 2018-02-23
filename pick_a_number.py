# practicepython.org exercise 9: guessing game one

import random

print("Welcome to the guessing game!!\n\nType 'exit' to quit\n" )
play = True

while play:
    number = random.randint(1,9)
    guesses = 1
    guess = input("\nGuess a number from 1 to 9:  \n")

    if guess == "exit":
        break

    while not isinstance(guess,int):
        if guess == "exit":
            break
        try:
            guess = int(guess)
            if guess not in range(1,10):
                print("That is not a valid option!\n")
                guess = input("Guess a number from 1 to 9:  \n")
        except ValueError:
            print("That is not a valid option!\n")
            guess = input("Guess a number from 1 to 9:  \n")
        
    if guess == 'exit':
        break
    while guess != number:
        if guess == 'exit':
            break
        if guess > number:
            print("You guessed too high.\n")
            guess = input("Guess again:  ")
        else:
            print("You guessed too low.\n")
            guess = input("Guess again:  \n")
        while not isinstance(guess,int):
            if guess == "exit":
                break
            try:
                guess = int(guess)
                if guess not in range(1,10):
                    print("That is not a valid option!\n")
                    guess = input("Guess a number from 1 to 9:  \n")
            except ValueError:
                print("That is not a valid option!\n")
                guess = input("Guess a number from 1 to 9:  \n")
        guesses += 1
    if guesses == 1:
        g = "guess"
    else:
        g = "guesses"
    if guess == 'exit':
        break
    print("You got it in {} {}!! The number was {}.\n".format(guesses,g,number))
    again = input("Play again (y/n)? \n")
    if again == 'n' or again == 'exit':
        play = False

