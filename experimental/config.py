                           ### MINI GAME PACK CONFIG ###
                ### name = value | description | options | [default] ###
                         ### Not All games have config options ###

# Changing any varibles in the main file may result in the project not working correctly #
# Changing any value out of the vaild range will result in the project not being able to run #
            ### This can be bypassed by disablling config_verify ###

config_verify = True # | checks the config for any invaild values | False, True | [True]
               ### Disablling this option may cause the project to break ###

### Guessing Game ###
secret_number = 0 # | Number that has to be guessed | 0: random or >0 | [0]

### Loading Screen Simulator ### ### Still to add
rand_text = ["loading random text", "I made this in 3 hours", "School is cringe", "Table", "Upside-down Table :)", "reeeeeeeeeeeeeeee", "Are you enjoying this?","why did I make this?", "Are you sure you want to stay and watch this?", "go and touch grass", ":D", ":)", "How can you enjoy this?", "(err://TooBoring)", "Ur bad get gud","ez", "gamin", "Your future is boring", "Help, im stuck inside the infinte loop","It's 3am go outside", "Cry about it"]
# ^ | Text that appears in the loading UI | Fully Customisable (req 1 entry) | ["loading random text", "I made this in 3 hours", "School is cringe", "Table", "Upside-down Table :)", "reeeeeeeeeeeeeeee", "Are you enjoying this?","why did I make this?", "Are you sure you want to stay and watch this?", "go and touch grass", ":D", ":)", "How can you enjoy this?", "(err://TooBoring)", "Ur bad get gud","ez", "gamin", "Your future is boring", "Help, im stuck inside the infinte loop","It's 3am go outside", "Cry about it"] 



### General ###
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO", "m"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]


numbers_guessed = []
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
### LSS Varibles ###
loading_finish = 2 # 2 - start menu, 1 - finished, 2 - in-progress
        # Text Bank 
rand_text = ["loading random text", "I made this in 3 hours", "School is cringe", "Table", "Upside-down Table :)", "reeeeeeeeeeeeeeee", "Are you enjoying this?","why did I make this?", "Are you sure you want to stay and watch this?", "go and touch grass", ":D", ":)", "How can you enjoy this?", "(err://TooBoring)", "Ur bad get gud","ez", "gamin", "Your future is boring", "Help, im stuck inside the infinte loop","It's 3am go outside", "Cry about it"]