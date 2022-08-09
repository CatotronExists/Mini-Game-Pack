# Contents
# line 9 Varibles
# line 44 functions
# line 151 program
from random import randint
from random import randint as dice
import time
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
min_range = 0
max_range = 0
guesses_left = 0

custom_setup = True
vaild_range_min = False
vaild_range_max = False
vaild_range_guess = False
vaild_range = False
gen_range = 0 # no. of numbers that are between min and max
###############################################
### Functions ###
### Guessing Game ###
def guess_check(): # Checks Guess
    global guesses_left
    global correct
    global guess_number
    global numbers
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
    if difficulty_select in gg_vaild_difficulty:
        if difficulty_select in gg_vaild_difficulty_easy:
            difficulty = 1
            guesses_left = 5
            min_range = 1
            max_range = 10
        elif difficulty_select in gg_vaild_difficulty_medium:
            difficulty = 2
            guesses_left = 7
            min_range = 1
            max_range = 50
        elif difficulty_select in gg_vaild_difficulty_hard:
            difficulty = 3
            guesses_left = 11
            min_range = 1
            max_range = 100
        elif difficulty_select in gg_vaild_difficulty_impossible:
            difficulty = 4
            guesses_left = 20
            min_range = 1
            max_range = 1000
        elif difficulty_select in gg_vaild_difficulty_custom:
            difficulty = 5
            custom_setup = False
            play_again = False
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


while program == True:
    while game_selected == 0:
        print("----------------------------------------------------")
        print("Mini Game Pack (cli based)                     v0.01\n")
        print("Guessing Game (1 / gg)\nRock Paper Scissors (2 / rps)")
        game_selected = str(input("Select a Game\n-->> "))
        if game_selected in vaild_games:
            if game_selected == "1" or game_selected == "gg":
                game_selected = 1
            elif game_selected == "2" or game_selected == "rps":
                game_selected = 2
        else:
            print("Invaild Option\n")
    while game_selected == 1: # Guessing Game
        print("Guessing Game Selected\nLoading...")
        time.sleep(randint(0,2))

        print("\n-----------------------------------------------")
        print("Guess the number v1.4")
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
    while game_selected == 2: # RPS
        print("Rock Paper Scissors Selected")
        print("will be added soon!")
        time.sleep(999)

