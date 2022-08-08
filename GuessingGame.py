from random import randint as dice
import time
### Code starts on line  ###
### For Custom Mode ###
custom_setup = True
vaild_range_min = False
vaild_range_max = False
vaild_range_guess = False
vaild_range = False
gen_range = 0 # no. of numbers that are between min and max
###                 ###
###                           Other                                                 ###
difficulty_select = 0
hint_numbers = [2, 3, 4, 5]
difficulty = 0
play_again = 1
hints = 99
game_play = True
correct = False
min_range = 0
max_range = 0
guesses_left = 0
###                                                                                 ###
###                         yes/no Vaild                                            ###
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]
###                                                                     ###
###           Vaild Characters on Difficulty Selection                  ###
vaild_difficulty = ["1", "e", "E", "easy", "Easy", "2", "m", "M", "medium", "Medium", "3", "h", "H", "hard", "Hard", "4", "i", "I", "impossible", "Impossible", "5", "c", "C", "custom", "Custom", "6", "cl", "CL", "change log", "Change Log"]
vaild_difficulty_easy = ["1", "e", "E", "easy", "Easy"]
vaild_difficulty_medium = ["2", "m", "M", "medium", "Medium"]
vaild_difficulty_hard = ["3", "h", "H", "hard", "Hard"]
vaild_difficulty_impossible = ["4", "i", "I", "impossible", "Impossible"]
vaild_difficulty_custom =["5", "c", "C", "custom", "Custom"]
vaild_difficulty_change = ["6", "cl", "CL", "change log", "Change Log"]
difficulty_name = ["none", "Easy", "Medium", "Hard", "Impossible", "Custom"]
###   Functions   ###

def guess_check(): # Checks Guess
    global guesses_left
    global correct
    global guess_number
    numbers_guessed.insert(guesses_left, guess_number) # Adds guess to 'guess list'   
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
    global play_again
    global guesses_left
    global guess_number
    global correct
    global difficulty
    global game_play
    if play_again in yes_responses: # if yes to play again
        play_again = 1
        guesses_left = -1
        guess_number = 0
        correct = 2
        time.sleep(1)         
    if play_again in no_responses: # if no to play again
        play_again = 0
        difficulty = -1
        game_play = False
        correct = False
        guesses_left = -1       
        print("-----------------------------------------------")

def difficulty_setup():
    global difficulty
    global guesses_left
    global difficulty_name
    global min_range
    global max_range
    global custom_setup
    global difficulty_select
    global play_again
    if difficulty_select in vaild_difficulty:
        if difficulty_select in vaild_difficulty_easy:
            difficulty = 1
            guesses_left = 5
            min_range = 1
            max_range = 10
        elif difficulty_select in vaild_difficulty_medium:
            difficulty = 2
            guesses_left = 7
            min_range = 1
            max_range = 50
        elif difficulty_select in vaild_difficulty_hard:
            difficulty = 3
            guesses_left = 11
            min_range = 1
            max_range = 100
        elif difficulty_select in vaild_difficulty_impossible:
            difficulty = 4
            guesses_left = 20
            min_range = 1
            max_range = 1000
        elif difficulty_select in vaild_difficulty_custom:
            difficulty = 5
            custom_setup = False
            play_again = False
        elif difficulty_select in vaild_difficulty_change:
            difficulty = 6
    else: 
        print("Invaild Option")
        difficulty_select = 0

def hint():
    global hints
    global custom_setup
    global difficulty
    global hint_numbers
    global yes_responses
    global no_responses
    if difficulty in hint_numbers:
        while hints == 99:
            hints = str(input("Hints (y/n) "))
            if hints in yes_responses:
                hints = True
                custom_setup = True
            elif hints in no_responses:
                hints = False
                custom_setup = True
            else: 
                print("Invaild Option\n")
                hints = 99
    else: hints == False      
###    
print("\n-----------------------------------------------")
print("Guess the number v1.4")
print("\nChoose a Difficulty\n")
print("Easy (1)")
print("Medium (2)")
print("Hard (3)")
print("Impossible (4)")
print("Custom (5)")
print("Change Logs (6)")
while difficulty_select == 0:
    difficulty_select = (input("-->> ")) # difficulty num, 1 = e, 2 = m, 3 = h, 4 = i, 5 = c , 6 = cl,
    difficulty_setup()
###                                                            ###
while game_play == True:
    while(game_play == True and play_again == True): # Game
        difficulty_setup()
        hint()
        print("-----------------------------------------------")
        print(difficulty_name[difficulty]+ " Difficulty\n")
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
 
    while (custom_setup == False): # Custom setup ### hints broken
        while vaild_range_min == False:
                min_range = input("\n---------------------------------------------------\nInput Minimum Number\n-->> ")   
                if min_range.isnumeric():
                    vaild_range_min = True
                    print(str(min_range) + " Chosen as Minimum\n---------------------------------------------------")
                else: print(" \nError: NaN (Not a Number)")            
        while vaild_range_max == False:
            max_range = input("What Should the Highest possible number be? \n-->> ")
            if(max_range.isnumeric()):     
                if(min_range > max_range):
                    print("\nError: Max Cannot be larger than min")
                elif(min_range == max_range):
                    print("\nError: Min and Max can't be the same")
                else: 
                    vaild_range_max = True
                    print(str(max_range) + " Chosen as Maximum")
                    print("\n---------------------------------------------------")
                    print("Min: " + str(min_range) + " | Max: " + str(max_range)+ "\n")
            else: print("\nError: NaN (Not a Number)")
        max_range = int(max_range) 
        min_range = int(min_range)
        gen_range = gen_range + (max_range - min_range)
        while vaild_range_guess == False:
            guesses_left = input("Enter Guess Limit\n-->> ")
            if guesses_left.isnumeric():
                guesses_left = int(guesses_left)
                if guesses_left < gen_range:
                    vaild_range_guess = True
                elif guesses_left == 0:
                    print("You cant have 0 guesses!")
                elif guesses_left > gen_range:
                    print("You cant have more guesses than the range!")
            else: print("\nError NaN (Not a Number)")   
        print("\n---------------------------------------------------")
        print("Min: " + str(min_range) + " | Max: " + str(max_range))
        print("You will have " +str(guesses_left)+ " guesses!")   
        hint()
        play_again = True
          
    while(difficulty == 6): # Change Log
        print("-----------------------------------------------")
        print("Guess the number          Current Version: v1.4\n")
        print("Version 1.4 | Optimization Update (8/08/2022)")
        print("- Complete rework of the code, much more optimised now!\n")
        print("Version 1.3 | Difficulty Update (5/08/2022)")
        print("- New Difficulty option, Choose between Easy, Medium,\nHard and Impossible.\nAdded Option to use letters/word to choose a difficulty.\nMedium and above have togglable hints (Higher/Lower).\nOptimised code by making it longer :)\nChange log can now be closed.\n")
        print("Version 1.2.1")
        print("- Removed prints used for testing\n")
        print("Version 1.2 (28/08/2022)")
        print("- Updated starting menu\n")
        print("Version 1.1 (27/08/2022)")
        print("- Play again option added\n")
        print("Version 1.0 (25/08/2022)")
        print("- Release\n")
        print("-----------------------------------------------")
        change_log_page = input("Close (y/y)\n-->> ")
        if change_log_page == 'y':
            difficulty = 0
        else: print("...")
