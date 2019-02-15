###### hangman game #####


"""
def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         o         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "please guess one letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))

        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
              print("You won!")
              print(" ".join(board))
              win = True
              break

    if not win:
         print("\n".join(stages[0:wrong + 1]))
         print("You lost! The answer is {}.".format(word))
            
              
hangman("clock")

"""

"""
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose! It was {}.".format(word))

hangman("pencil")       
"""
import random


def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|         |         ",
              "|         |         ",
              "|         o         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              "|___________________"                   
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "please guess one letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))

        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "_" not in board:
              print("You won!")
              print(" ".join(board))
              win = True
              break

    if not win:
         print("\n".join(stages[0:wrong + 1]))
         print("You lost! The answer is {}.".format(word))
            

list_of_words = ["desk", "chair", "book", "note", "pencil"]

n = random.randint(0, 4)
           
hangman(list_of_words[n])  
        






    
              
