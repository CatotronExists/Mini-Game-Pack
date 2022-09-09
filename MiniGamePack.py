# Contents
# line 9 Varibles
# line 51 functions
# line 112 program
from random import randint
from random import randint as dice
import time
hider = True
if hider == True:
    ### Game Menu ###
    game_selected = 0 # 0 - no game/menu, 1 - GuessingGame, 2 - RPS,
    vaild_games = ["1", "gg", "2", "rps"]
    program = True
    ### General ###
    vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO", "m"]
    yes_responses = ["yes", "y","Yes", "YES"]
    no_responses = ["no", "n","No", "NO"]
    ### Guessing Game Varibles ###
    gg_vaild_difficulty = ["1", "e", "E", "easy", "Easy", "2", "m", "M", "medium", "Medium", "3", "h", "H", "hard", "Hard", "4", "i", "I", "impossible", "Impossible", "5", "c", "C", "custom", "Custom"]
    gg_vaild_difficulty_easy = ["1", "e", "E", "easy", "Easy"]
    gg_vaild_difficulty_medium = ["2", "m", "M", "medium", "Medium"]
    gg_vaild_difficulty_hard = ["3", "h", "H", "hard", "Hard"]
    gg_vaild_difficulty_impossible = ["4", "i", "I", "impossible", "Impossible"]
    gg_vaild_difficulty_custom =["5", "c", "C", "custom", "Custom"]
    gg_difficulty_name = ["none", "Easy", "Medium", "Hard", "Impossible", "Custom"]

    difficulty_select = 0
    hint_numbers = [2, 3, 4, 5]
    difficulty = 0
    play_again = 1
    hints = 99
    game_play = True
    correct = False
    min_range = 1
    max_range = guesses_left = custom_guesses = 0 # all var = 0

    custom_setup = True # Starts as True to skip setup if custom not chosen
    vaild_range_min = vaild_range_guess = vaild_range_max = vaild_range = False
    gen_range = 0 # no. of numbers that are between min and max
    ### RPS Varibles ### 
    computer_options = ["Rock", "Paper", "Scissors"]
    options = ["1","r", "R", "Rock", "rock", "2", "p", "P", "Paper", "paper", "3","s", "S", "Scissors", "scissors"]
    rock_options = ["r", "R", "Rock", "rock", "1"]
    paper_options = ["p", "P", "Paper", "paper", "2"]
    scissor_options = ["s", "S", "Scissors", "scissors", "3"]
    player_choice = 0 # 0 - unset, 1 - rock, 2 - paper, 3 - scissors
    player_choice_set = False
    computer_choice = computer_choice_num = player_choice_num = 0
    play_again = True
    ###############################################
    ### Functions ###
    ### Guessing Game ###
    def guess_check(): # Checks Guess
        global guesses_left, correct, guess_number
        numbers_guessed.insert(999, guess_number) # Adds guess to 'guess list'   
        guesses_left = guesses_left - 1 # lowers guesses left on each guess
        if guess_number == secret_number:
            correct = True
        else:
            correct = False
            print("You guessed the wrong number! You still have "+str(guesses_left)+" Attempt(s)")
            if(guess_number > max_range):
                print("Invaild Number (Too High)") 
            if(guess_number < min_range):
                print("Invaild Number (Too Low)")
            if hints == True:                        
                if(guess_number < secret_number):
                    print("The Secret Number is Higher!\n ")
                if(guess_number > secret_number):
                    print("The Secret Number is Lower\n ")

    def gg_playagain():
        global guesses_left, guess_number, correct, play_again
        guesses_left = -1
        guess_number = 0
        correct = 2
        play_again = True
        time.sleep(1) 

    def difficulty_setup():
        global difficulty, guesses_left, min_range, max_range, custom_setup, difficulty_select, play_again
        if difficulty_select in gg_vaild_difficulty:
            if difficulty_select in gg_vaild_difficulty_easy: difficulty, guesses_left, max_range = 1, 5, 10 #easy
            elif difficulty_select in gg_vaild_difficulty_medium: difficulty, guesses_left, max_range = 2, 7, 50 #medium
            elif difficulty_select in gg_vaild_difficulty_hard: difficulty, guesses_left, max_range = 3, 11, 100 #hard
            elif difficulty_select in gg_vaild_difficulty_impossible: difficulty, guesses_left, max_range = 4, 20, 1000 #impossible
            elif difficulty_select in gg_vaild_difficulty_custom: #custom
                difficulty = 5
                if custom_setup != False: custom_setup = False
                play_again = False
                guesses_left = custom_guesses
        else: 
            print("Invaild Option")
            difficulty_select = 0

    def hint():
        global hints, custom_setup, difficulty, hint_numbers, yes_responses, no_responses
        if difficulty in hint_numbers:
            while hints == 99: 
                hints = str(input("Hints (y/n)\n-->> "))
                if hints in yes_responses: 
                    hints = True
                    print("Hints Enabled")
                elif hints in no_responses:
                    hints = False
                    print("Hints Disabled")
                else: 
                    print("Invaild Option\n")
                    hints = 99
        else: hints == False

while program == True:
    while game_selected == 0:
        print("----------------------------------------------------")
        print("Mini Game Pack (cli based)                    v0.2.1\n")
        print("Guessing Game (1 / gg)\nRock Paper Scissors (2 / rps)\n??? (Coming in v0.3)\n??? (coming in v0.5)\nPage 1 of 1\n----------------------------------------------------")
        game_selected = str(input("Select a Game\n-->> "))
        play_again = True
        if game_selected in vaild_games:
            if game_selected == "1" or game_selected == "gg": game_selected = 1
            elif game_selected == "2" or game_selected == "rps": game_selected = 2
            elif game_selected == "3" or game_selected == "lss": game_selected = 3
        else: print("Invaild Option\n")
       
    while game_selected == 1 and play_again == True: # Guessing Game
        print("Guessing Game Selected\nLoading...")
        time.sleep(randint(0,2))
        print("\n-----------------------------------------------")
        print("Guess The Number")
        print("\nChoose a Difficulty")
        print("Easy (1)\nMedium (2)\nHard (3)\nImpossible (4)\nCustom (5)")
        while difficulty_select == 0: # setup
            difficulty_select = (input("-->> ")) # difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = c , 6 = cl,
            difficulty_setup()
        if custom_setup == False: # Custom setup 
            min_range = max_range = custom_guesses = 0
            hints = 99
            while min_range == 0:  # Min
                min_range = int(input("\n---[Custom Difficulty Setup]---\nInput Minimum Number...\n-->> "))
                print(str(min_range) + " Chosen as Minimum\n")
            while max_range == 0: # Max
                max_range = int(input("Input Maxmium Number...\n-->> "))
                if min_range > max_range:
                    print("\nError: Max Cannot be larger than min")
                    max_range = 0
                elif(min_range == max_range):
                    print("\nError: Min and Max can't be the same")
                    max_range = 0
                else: 
                    print(str(max_range) + " Chosen as Maximum")
                    print("\n---------------------------------------------------\nMin: " + str(min_range) + " | Max: " + str(max_range)+ "\n")
                    gen_range = gen_range + (max_range - min_range)
            while custom_guesses == 0: # Custom
                custom_guesses = int(input("Enter Guess Limit\n-->> "))
                if custom_guesses < gen_range:
                    print("\n---------------------------------------------------\nMin: " + str(min_range) + " | Max: " + str(max_range) + " You will have " +str(custom_guesses)+ " guesses!")   
                elif custom_guesses == 0: 
                    print("You cant have 0 guesses!")
                elif custom_guesses > gen_range:
                    print("You cant have more guesses than the range!")
                    custom_guesses = 0  
            hint()
            play_again = True
        while(play_again == True): # Game
            difficulty_setup()
            hint()
            print("-----------------------------------------------")
            print(gg_difficulty_name[difficulty]+ " Difficulty\n")
            print("A number from " +str(min_range)+ " to " +str(max_range)+ " will be chosen at random")
            print("You will have " +str(guesses_left)+ " guesses to find the correct number")
            numbers_guessed = []
            secret_number = dice(min_range, max_range) 
            print("\nYou have "+str(guesses_left)+ " guesses left")
            while(guesses_left > 0): # Guesses still remaining
                guess_number = int(input("\nPut your guess here: ")) # Forces an int value
                guess_check()                   
                if correct == False:
                    if(guesses_left == 0): # Out of guesses
                        print("\nYou ran out of guesses! The correct number was "+str(secret_number)+"!\n\nYour guesses were;") 
                        print(numbers_guessed)  
                        play_again = input("\nPlay again? (y/n) or Return to Menu (m)\n-->> ")
                        if play_again in yes_responses: gg_playagain()
                        elif play_again == "m": game_selected = difficulty_select = 0 
                        else: play_again = False
                
                if(correct == True):
                    print("You guessed the correct number!\n\nYour guesses were;")
                    print(numbers_guessed)
                    play_again = input("\nPlay again? (y/n) or Return to Menu (m)\n-->> ")
                    if play_again in yes_responses: gg_playagain()
                    elif play_again == "m": game_selected = difficulty_select = 0  
                    else: play_again = False

    while game_selected == 2 and play_again == True: # RPS
        print("Rock Paper Scissors Selected\nLoading...")
        time.sleep(randint(0,2))
        while play_again == True:
            computer_choice = computer_options[randint(0,2)]
            while player_choice_set == False:
                player_choice = input("\n------------------------------------------\nRock Paper Scissors                     \nWhat do you throw?\nRock, Paper or Scissors?\n-->> ")
                if player_choice in options:
                    if player_choice in rock_options: player_choice = "Rock"
                    elif player_choice in paper_options: player_choice = "Paper"                    
                    elif player_choice in scissor_options: player_choice = "Scissors"
                    player_choice_set = True          
                else:
                    print("Invaild Option")
                    player_choice_set = False                
            print("\nYou threw " +str(player_choice))
            time.sleep(0.5)
            print("Computer threw " +str(computer_choice))
            if computer_choice == "Rock": computer_choice_num = 1
            elif computer_choice == "Paper": computer_choice_num = 2
            elif computer_choice == "Scissors": computer_choice_num = 3

            if player_choice == "Rock": player_choice_num = 1
            elif player_choice == "Paper": player_choice_num = 2
            elif player_choice == "Scissors": player_choice_num = 3

            if player_choice_num == computer_choice_num: print("It's a tie, No one wins!")
            elif player_choice_num > computer_choice_num: print("You Win!")
            elif player_choice_num < computer_choice_num: print("You Lost!")    
            play_again = input("Play again? (y/n) or Return to Menu (m)\n-->> ")
            if play_again in yes_responses:
                player_choice_set = False
                play_again = True
                time.sleep(0.3)
            elif play_again == "m": 
                game_selected = 0    
                player_choice_set = False
            else: 
                play_again = False
                print("...\n-------------------------------------")
