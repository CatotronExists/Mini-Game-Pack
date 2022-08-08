from random import randint
import time
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
computer_options = [1, 2, 3]
computer_letter_options = ["Rock", "Paper", "Scissors"]
player_letter_options = ["Rock", "Paper", "Scissors"]
options = ["1","r", "R", "Rock", "rock", "2", "p", "P", "Paper", "paper", "3","s", "S", "Scissors", "scissors"]
rock_options = ["r", "R", "Rock", "rock", "1"]
paper_options = ["p", "P", "Paper", "paper", "2"]
scissor_options = ["s", "S", "Scissors", "scissors", "3"]
player_choice = 0 # 0 - unset, 1 - rock, 2 - paper, 3 - scissors
player_choice_set = False
computer_choice = 0
play_again = True

def vaild():
    global player_choice_set
    player_choice_set = True
    print("\nYou threw " +str(player_choice))

def player_convert():
    global player_choice
    global player_letter_options
    if player_choice in rock_options:
        player_choice = "Rock"
    elif player_choice in paper_options:
        player_choice = "Paper"
    elif player_choice in scissor_options:
        player_choice = "Scissors"

def com_convert():
    global computer_choice
    global computer_letter_options
    if computer_choice == 1:
        computer_letter_options = computer_letter_options[0]
    elif computer_choice == 2:
        computer_letter_options = computer_letter_options[1]
    elif computer_choice == 3:
        computer_letter_options = computer_letter_options[2]

def lost():
    global player_choice_set
    print("You Lost!")
    player_choice_set = False

def won():
    global player_choice_set
    print("You Win!")
    player_choice_set = False

while play_again == True:
    play_again = False
    computer_choice = computer_options[randint(0,2)]
    com_convert()
    while player_choice_set == False:
        player_choice = input("What do you throw?\nRock, Paper or Scissors?\n-->> ")
        if player_choice in options:
            player_convert()
            while player_choice_set == False:
                if player_choice in rock_options:
                    vaild()
                    player_choice = 1
                elif player_choice in paper_options:
                    vaild()
                    player_choice = 2
                elif player_choice in scissor_options:
                    vaild()
                    player_choice = 3 
        else:print("Invaild Option\n")
    while player_choice_set == True:
        print("Computer threw " +str(computer_letter_options))
        if player_choice == computer_choice:
            print("It's a tie, No one wins!")
            player_choice_set = False
        else:
            if player_choice == 1: # Rock
                if computer_choice == 2: # Rock (p) v Paper 
                    lost()
                elif computer_choice == 3: # Rock (p) v Scissors
                    won()
            elif player_choice == 2: # Paper
                if computer_choice == 1: # Paper (p) v Rock
                    won()
                elif computer_choice == 3: # Paper (p) v Scissors
                    lost()
            elif player_choice == 3: # Scissors
                if computer_choice == 1: # Scissors (p) v Rock
                    lost()
                elif computer_choice == 2: # Scissors (p) v Paper
                    won()