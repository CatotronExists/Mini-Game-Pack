# Contents
# line 9 Varibles
# line 52 functions
# line 139 program
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
    vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
    yes_responses = ["yes", "y","Yes", "YES"]
    no_responses = ["no", "n","No", "NO"]
    ### Guessing Game Varibles ###
    gg_vaild_difficulty = ["1", "e", "E", "easy", "Easy", "2", "m", "M", "medium", "Medium", "3", "h", "H", "hard", "Hard", "4", "i", "I", "impossible", "Impossible", "5", "c", "C", "custom", "Custom", "6", "cl", "CL", "change log", "Change Log"]
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

    custom_setup = True
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
    computer_choice = 0
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

    def playagain():
        global play_again, guesses_left, guess_number, correct, difficulty, game_play, custom_guesses
        if play_again in yes_responses: # if yes to play again
            play_again = 1
            if game_selected == 1:
                guesses_left = -1
                guess_number = 0
                correct = 2
                time.sleep(1)         
        if play_again in no_responses: # if no to play again
            play_again = 0
            if game_selected == 1:
                difficulty = guesses_left = -1
                game_play = correct = False      
                print("-----------------------------------------------")

    def difficulty_setup():
        global difficulty, guesses_left, min_range, max_range, custom_setup, difficulty_select, play_again
        if difficulty_select in gg_vaild_difficulty:
            if difficulty_select in gg_vaild_difficulty_easy:
                difficulty, guesses_left, max_range = 1, 5, 10
            elif difficulty_select in gg_vaild_difficulty_medium:
                difficulty, guesses_left, max_range = 2, 7, 50
            elif difficulty_select in gg_vaild_difficulty_hard:
                difficulty, guesses_left, max_range = 3, 11, 100
            elif difficulty_select in gg_vaild_difficulty_impossible:
                difficulty, guesses_left, max_range = 4, 20, 1000 
            elif difficulty_select in gg_vaild_difficulty_custom:
                difficulty = 5
                custom_setup = play_again = False
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
                    hints = custom_setup = True
                elif hints in no_responses:
                    hints = False
                    custom_setup = True
                else: 
                    print("Invaild Option\n")
                    hints = 99
        else: hints == False
    ### RPS Functions ###
    def vaild():
        global player_choice_set
        player_choice_set = True
        print("\nYou threw " +str(player_choice))
        time.sleep(1)

    def lost():
        global player_choice_set
        print("You Lost!")
        player_choice_set = False

    def won():
        global player_choice_set
        print("You Win!")
        player_choice_set = False

while program == True:
    while game_selected == 0:
        print("----------------------------------------------------")
        print("Mini Game Pack (cli based)                      v0.2\n")
        print("Guessing Game (1 / gg)\nRock Paper Scissors (2 / rps)")
        game_selected = str(input("Select a Game\n-->> "))
        if game_selected in vaild_games:
            if game_selected == "1" or game_selected == "gg":
                game_selected = 1
            elif game_selected == "2" or game_selected == "rps":
                game_selected = 2
        else:
            print("Invaild Option\n")
    while game_selected == 1 and play_again == True: # Guessing Game
        print("Guessing Game Selected\nLoading...")
        time.sleep(randint(0,2))
        print("\n-----------------------------------------------")
        print("Guess the number")
        print("\nChoose a Difficulty\n")
        print("Easy (1)")
        print("Medium (2)")
        print("Hard (3)")
        print("Impossible (4)")
        print("Custom (5)")
        while difficulty_select == 0:
            difficulty_select = (input("-->> ")) # difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = c , 6 = cl,
            difficulty_setup()
        while game_play == True:
            while(game_play == True and play_again == True): # Game
                difficulty_setup()
                hint()
                print("-----------------------------------------------")
                print(gg_difficulty_name[difficulty]+ " Difficulty\n")
                print("A number from " +str(min_range)+ " to " +str(max_range)+ " will be chosen at random")
                print("You will have " +str(guesses_left)+ " guesses to find the correct number")
                numbers_guessed = []
                secret_number = dice(min_range, max_range) 
                print("\nYou have "+str(guesses_left)+ " guesses left")
                while(guesses_left > 0):
                    guess_number = int(input("\nPut your guess here: ")) # Forces an int value
                    guess_check()                   
                    if correct == False:
                        while(guesses_left == 0):
                            guesses_left = False
                            print("\nYou ran out of guesses! The correct number was "+str(secret_number)+"!\n\nYour guesses were;") 
                            print(numbers_guessed)  
                            play_again = str(input("\nPlay again? (y/n) "))
                            if play_again in vaild_responses:
                                playagain()
                                if play_again in no_responses:
                                    break
                            else: print("Invaild Choice (y/n)")    
                    while(correct == True):
                        print("You guessed the correct number!\n\nYour guesses were;")
                        print(numbers_guessed)
                        play_again = str(input("\nPlay again? (y/n) "))
                        if play_again in vaild_responses:
                            playagain()
                            if play_again in no_responses:
                                break
                        else: print("Invaild Choice (y/n)")     

            while (custom_setup == False): # Custom setup
                while vaild_range_min == False:
                        min_range = int(input("\n---------------------------------------------------\nInput Minimum Number\n-->> "))   
                        vaild_range_min = True
                        print(str(min_range) + " Chosen as Minimum\n---------------------------------------------------")           
                while vaild_range_max == False:
                    max_range = int(input("What Should the Highest possible number be? \n-->> "))  
                    if(min_range > max_range):
                        print("\nError: Max Cannot be larger than min")
                    elif(min_range == max_range):
                        print("\nError: Min and Max can't be the same")
                    else: 
                        vaild_range_max = True
                        print(str(max_range) + " Chosen as Maximum")
                        print("\n---------------------------------------------------\nMin: " + str(min_range) + " | Max: " + str(max_range)+ "\n")
                        gen_range = gen_range + (max_range - min_range)
                while vaild_range_guess == False:
                    custom_guesses = int(input("Enter Guess Limit\n-->> "))
                    if custom_guesses < gen_range:
                        vaild_range_guess = True
                        print("\n---------------------------------------------------\nMin: " + str(min_range) + " | Max: " + str(max_range) + " You will have " +str(custom_guesses)+ " guesses!")   
                        hint()
                        play_again = True
                    elif custom_guesses == 0:
                        print("You cant have 0 guesses!")
                    elif custom_guesses > gen_range:
                        print("You cant have more guesses than the range!")  
                
    while game_selected == 2 and play_again == True: # RPS
        print("Rock Paper Scissors Selected\nLoading...")
        time.sleep(randint(0,2))
        while play_again == True:
            play_again = False
            computer_choice = computer_options[randint(0,2)]
            while player_choice_set == False:
                player_choice = input("------------------------------------------\nRock Paper Scissors                     \nWhat do you throw?\nRock, Paper or Scissors?\n-->> ")
                if player_choice in options:
                    while player_choice_set == False:
                        if player_choice in rock_options:
                            player_choice = "Rock"
                            vaild()     
                        elif player_choice in paper_options:
                            player_choice = "Paper"
                            vaild()                    
                        elif player_choice in scissor_options:
                            player_choice = "Scissors" 
                            vaild()
                else:print("Invaild Option\n")
            while player_choice_set == True:
                print("Computer threw " +str(computer_choice))
                if player_choice == computer_choice:
                    print("It's a tie, No one wins!")
                    player_choice_set = False
                else:
                    if player_choice == "Rock": # Rock
                        if computer_choice == "Paper": # Rock (p) v Paper 
                            lost()
                        elif computer_choice == "Scissors": # Rock (p) v Scissors
                            won()
                    elif player_choice == "Paper": # Paper
                        if computer_choice == "Rock": # Paper (p) v Rock
                            won()
                        elif computer_choice == "Scissors": # Paper (p) v Scissors
                            lost()
                    elif player_choice == "Scissors": # Scissors
                        if computer_choice == "Rock": # Scissors (p) v Rock
                            lost()
                        elif computer_choice == "Paper": # Scissors (p) v Paper
                            won()
            while play_again == False:
                play_again = input("Play again? (y/n)\n-->> ")
                if play_again in vaild_responses:
                    if play_again in yes_responses:
                        print("")
                        play_again = True
                    elif play_again in no_responses:
                        print("...\n-------------------------------------")
                else:print("Invaild Option")   
