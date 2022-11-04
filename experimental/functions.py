from config import *
from libraries import *
from globals import *
### Guessing Game ###
def guess_check(): # Checks Guess
    global guesses_left, correct, guess_number, numbers_guessed, secret_number
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

### Other ###
def close():
    global play_again
    play_again = False
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n------------------------------------")

def invaild():
    from MiniGamePack import vaild    
    vaild = False
    print("Invaild Option")
    time.sleep(0.5)