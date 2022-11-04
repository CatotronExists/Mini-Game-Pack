from functions import *
from config import *
from libraries import *
from menus import *
from globals import *

### Game Menu ###
game_selected = 0 # 0 - no game/menu, 1 - GuessingGame, 2 - RPS, 3 - LSS
program = True
page = 1 
vaild = True

while program == True: # Makes switching games possible/play again system
    while game_selected == 0: # Main Menu
        main_menu_ui()
        from menus import game_selected
        
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
                        else: close()
                
                if(correct == True):
                    print("You guessed the correct number!\n\nYour guesses were;")
                    print(numbers_guessed)
                    play_again = input("\nPlay again? (y/n) or Return to Menu (m)\n-->> ")
                    if play_again in yes_responses: gg_playagain()
                    elif play_again == "m": game_selected = difficulty_select = 0  
                    else: close()

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
            else: close()
    
    if game_selected == 3 and play_again == True: # Stops the message showing up when playing lss again
        print("Loading Screen Simulator Selected\nLoading...")
        time.sleep(randint(1,2))
        while game_selected == 3 and play_again == True: # Loading Screen Sim
            while loading_finish == 2:
                loading_progress = loading_int = display_update = loading_finish = delay = last_loading_progress = timer = 0
                end2 = 999
                progress_numbers = []
                progress_delays = []
                start = time.time() # Timer starts
                print("\n----------------------------------------------------------------------------------------------------")
                print("Loading Screen Simulator                                                                        v1.0")
                print("\nNow Loading...")
                print("█"*loading_progress) # Multiplies the times the character prints based on the progress
                print("                                                                                                 "+str(loading_progress)+"%")
                print("why are you here?")
                print("                                                                           ┬─┬                     ")
                print("----------------------------------------------------------------------------------------------------\n")
                sleep(1) # Delay added so loading progress doesnt start instantly

            while(loading_finish == 0):
                if(loading_finish != 1):
                    last_loading_progress = loading_progress
                    delay = (randint(0, 10)+loading_int/5) # Calcuation of time between each progress (a tick)
                    sleep(delay)
                    delay = int(delay) 
                    progress_delays.insert(100, delay) # Helps Debug Menu
                    loading_progress += randint(1, 500) # How much the Progress goes up by each tick
                    progress_numbers.insert(100, loading_progress) # Helps Debug menu
                    loading_int += randint(1, 2) # Increases loading interval (time between progress)
                    display_update = 1
                if(loading_progress > 100):
                    loading_finish = 1
                    loading_progress = 100 # If the % goes over 100 it gets pushed back down

                if(display_update == 1):
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("Loading Screen Simulator                                                                        v1.0\n")
                    print("Now Loading...")
                    print("█"*loading_progress) # Multiplies the times the character prints based on the progress
                    print("                                                                                                 "+str(loading_progress)+"%")
                    print(rand_text[randint(0, 20)]) # Choses a random index in the random text list
                    print("                                                                           (╯°□°）╯︵ ┻━┻           ")
                    print("----------------------------------------------------------------------------------------------------\n")
                
                if(loading_finish == 1):
                    end = time.time() # Ends timer
                    timer = end-start # Setup for Debug
                    timer = int(timer)
                    print("\n----------------------------------------------------------------------------------------------------")
                    print("Loading Screen Simulator                                                                        v1.0\n")
                    print("Now Loading")
                    print("█"*loading_progress) # Multiplies the times the character prints based on the progress
                    print("                                                                                                 "+str(loading_progress)+"%")
                    print("Wow you really did just watch a progress bar for that long?")
                    print(str(timer)+ " Seconds wasted") # Displays how long the loading process took
                    print("                                                                           ┬─┬ ノ( ゜-゜ノ)          ")
                    print("----------------------------------------------------------------------------------------------------\n")
                    end = input("Start over? (y/n)\nor Return to Menu (m) ") # To keep the window open after loading finishes

            if(end == 'debug'):
                print("----------------------------------------------------------------------------------------------------")
                print("Debug menu")
                print("Time Elapsed "+str(timer) +" (Seconds)\n")
                print("Progress Numbers")
                print(progress_numbers)
                print("\nProgress Delays")
                print(progress_delays)
                print("\n(╯°□°）╯︵ ┻━┻")
                print("Version 1.0")
                print("----------------------------------------------------------------------------------------------------")
                end = input("") # Keeps debug open [Enter] to close
            elif(end in yes_responses):
                loading_finish = 2
                print("Resetting Progress...")
                time.sleep(0.75)
            elif(end == "m"): 
                game_selected = 0
                loading_finish = 2
            else:
                print("\nClosing...")
                play_again = False
                time.sleep(1)