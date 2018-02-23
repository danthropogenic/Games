# hangman game code


import random

word_list = []
with open('hangman_words.txt','r') as hw:
    word_list = hw.read().split('\n')


def hangman():
    word_num = random.randint(0,len(word_list)-1)
    word = word_list[word_num]
    wrong = 0
    stages = ["""
              _________        
              |        |       
              |              
              |             
              |             
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |             
              |             
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |        |     
              |             
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |       /|      
              |             
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |       /|\      
              |             
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |       /|\      
              |       /     
              |________________""",
              """
              _________        
              |        |       
              |        O       
              |       /|\      
              |       / \      
              |________________"""
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman! \n\n")
    print(" ".join(board))

    while wrong < len(stages):
        print('\n')
        if "_" not in board:
                print("You Win!!")
                print(" ".join(board))
                win = True
                break
        msg = ("Guess a letter:  ")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
            if "_" in board:
                print("\n You Got One!! \n\n" + " ".join(board))
        elif char in board:
            print("\nYou already guessed '{}' you silly goose!".format(char))
        else:
            print("\n'{}' is not in the word".format(char))
            print(stages[wrong])
            wrong += 1
            print(" ".join(board))
                  
    if not win:
        print("You lost! The word was {}.".format(word))
