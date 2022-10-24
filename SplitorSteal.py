from libraries import *
from config import *
# PowerUps: 
# a rough estimate on what the other player chose, 
# a guarantee you get 25% of the money (even if both steal), 
# double win/double loss: if you win money you gain twice the amount, but if you lose you lose double the winnings

vaild = False
mode = 0
player1_choice = 0 # Player 1 is also the player vs Computer
player2_choice = 0 # Player 2 is also the computer in (vs computer mode)
choice_list = ["na", "Split", "Steal"]
play_again = False # False until config checks
config_errors = 0

def invaild():
    global vaild
    vaild = False
    print("Invaild Option")
    time.sleep(0.5)
        
def player1():
    global player1_choice, choice_list, player1_choice, vaild, input
    vaild = False
    while vaild == False:
        player1_choice = int(input("Player 1, Will you Split (1) or Steal (2)?\n-->> "))
        if player1_choice == 1 or player1_choice == 2:
            print("You chose to "+str(choice_list[player1_choice])+"") # Gets player choice
            print("Press [ENTER] to hide your pick!")
            input("")
            print("\n" * 999)
            vaild = True
        else: invaild()

def player2():
    global player2_choice, choice_list, player2_choice, vaild, input
    vaild = False
    while vaild == False:
        player2_choice = int(input("Player 2, Will you Split (1) or Steal (2)?\n-->> "))
        if player2_choice == 1 or player2_choice == 2:
            print("You chose to "+str(choice_list[player2_choice])+"") # Gets player choice
            print("Press [ENTER] to hide your pick!")
            input("")
            print("\n" * 999)
            vaild = True
        else: invaild()

if config_verify == True: # checks config for invaild options
    if player1_bal < 0:
        print("player1_bal has an invaild value, check config.py")
        config_errors += 1
    elif player2_bal < 0: 
        print("player2_bal has an invaild value, check config.py")
        config_errors += 1
    elif first < 0: 
        print("first has an invaild value, check config.py")
        config_errors += 1
    elif reward < 0 and reward >999: 
        print("reward has an invaild value, check config.py")
        config_errors += 1
    elif starting_guide == False or starting_guide == True: 
        print("\n")
    else:
        print("starting_guide has an invaild value, check config.py")
        config_errors += 1

if config_errors != 0: 
    print(str(config_errors)+" Error(s) Found in config.py")
    input("")
else: play_again = True
            
while play_again == True:
    vaild = False
    mode = 0
    player1_choice = 0
    player2_choice = 0
    print("...Split Or Steal...") 
    if starting_guide == True:
        print("A Game about predicting the other player's choice\nYou have two options in front of you, Split or Steal.\nThe rules are simple, If both players Split the money will get split\nBut if one player Steals they get all the money, If both players are to Steal neither get anything.")
        starting_guide = False
    while vaild == False:
        print("\nPlay Against an Computer (c) or another Person (p) [You will Have to pass the device to the other player]")
        vaild = input("-->> ")
        if vaild == "c":
            mode = "Computer" # 1
        elif vaild == "p": 
            mode = "Player" # 2
            print("")
        else: invaild()
    print("You have chosen to play against "+mode+" ")
    from config import reward
    if reward == 0:
        reward = dice(0,999)
    print("There is $"+str(reward)+" up for grabs")

    if mode == "Computer":
        if first != 0: # checks if config was changed
            if (first % 2) == 0:
                first = 2
            else: first = 1
        else: first = dice(1,2) # Randomly decides who goes first
        time.sleep(0.5)
        if first == 1:
            print("You will be chosing First")
            vaild = False
            while vaild == False: # Player choice
                player1_choice = int(input("\nWill you Split (1) or Steal (2)?\n-->> "))
                if player1_choice == 1 or player1_choice == 2:
                    print("You chose to "+str(choice_list[player1_choice])+"") # Gets player 1 choice
                    vaild = True
                else: invaild()
            time.sleep(0.3)
            print("Computer is chosing...")
            player2_choice = dice(1,2)
            time.sleep(random.random())
            print("Computer has chosen\n")
            time.sleep(0.7)
        elif first == 2:
            print("You will be chosing Second")
            time.sleep(0.3)
            print("Computer is chosing...")
            player2_choice = dice(1,2)
            time.sleep(random.random())
            print("Computer has chosen, It's your turn now...")
            time.sleep(0.7)
            vaild = False
            while vaild == False: # Player choice
                player1_choice = int(input("\nWill you Split (1) or Steal (2)?\n-->> "))
                print(player1_choice)
                if player1_choice == 1 or player1_choice == 2:
                    print("You chose to "+str(choice_list[player1_choice])+"") # Gets player 1 choice
                    vaild = True
                else: invaild()
        
        print("Both Players have chosen,")
        time.sleep(0.5)
        first = dice(1,2)
        if first == 1:
            print("You chose to... "+str(choice_list[player1_choice])+"")
            time.sleep(random.random())
            print("Computer chose to... "+str(choice_list[player2_choice])+"")
        
        if first == 2:
            print("Computer chose to... "+str(choice_list[player2_choice])+"")
            time.sleep(random.random())
            print("You chose to... "+str(choice_list[player1_choice])+"")

        time.sleep (0.4)
        if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Steal": # Both users said Steal
            print("\nBecause Both Players chose to Steal, Neither of you get anything.\n$"+str(reward)+" lost to the v o i d")
        if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Split": # Both users said Split 
            reward = (reward / 2)
            print("\nBoth Players Chose to Split, Both Players will recieve the same amount of Money [$"+str(reward)+"]") 
            player1_bal += reward
            player2_bal += reward
        if choice_list[player1_choice] == "Steal" and choice_list[player2_choice] == "Split": # P1 Stole from P2
            print("\nYou Stole all the Money from Computer [$"+str(reward)+"]")
            player1_bal += reward
        if choice_list[player2_choice] == "Steal" and choice_list[player1_choice] == "Split": # P2 Stole from P1
            print("\nComputer Stole all the Money from You [$"+str(reward)+"]")
            player2_bal += reward
                
    if mode == "Player":
        print("A Player will be chosen to go first,")
        first = dice(1,2)
        print("Player "+str(first)+" will be chosing First\nPass the Device to Player "+str(first)+" and press [ENTER]")
        input("")
        if first == 1: player1()
        elif first == 2: player2()   
        print("Pass the Device to other player and press [ENTER]")
        input("")
        if first == 1: player2() # Reversed to make second player pick
        elif first == 2: player1()
        print("Once the screen is Visible to both players press [ENTER]")
        input("")
        print("Both Players have chosen,")
        time.sleep(0.5)
        first = dice(1,2)
        if first == 1:
            print("Player 1 chose to... "+str(choice_list[player1_choice])+"")
            time.sleep(random.random())
            print("Player 2 chose to... "+str(choice_list[player2_choice])+"")
        
        if first == 2:
            print("Player 2 chose to... "+str(choice_list[player2_choice])+"")
            time.sleep(random.random())
            print("Player 1 chose to... "+str(choice_list[player1_choice])+"")
        
        if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Steal": # Both users said Steal
            print("\nBecause Both Players chose to Steal, Neither of you get anything.\n$"+str(reward)+" lost to the v o i d")
        if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Split": # Both users said Split 
            reward = (reward / 2)
            print("\nBoth Players Chose to Split, Both Players will recieve the same amount of Money [$"+str(reward)+"]")
            player1_bal += reward
            player2_bal += reward
        if choice_list[player1_choice] == "Steal" and choice_list[player2_choice] == "Split": # P1 Stole from P2
            print("\nPlayer 1 Stole all the Money from Player 2 [$"+str(reward)+"]")
            player1_bal += reward
        if choice_list[player2_choice] == "Steal" and choice_list[player1_choice] == "Split": # P2 Stole from P1
            print("\nPlayer 2 Stole all the Money from Player 1 [$"+str(reward)+"]")
            player2_bal += reward
        
    print("Player 1 now has...$"+str(player1_bal))
    print("Player 2 now has...$"+str(player2_bal))
    time.sleep(0.7)
    play_again = input("\nPlay Again? (y/n) ")
    if play_again == 'y':
        play_again = True
        print("")
    elif play_again == 'n':
        play_again = False
        print("Game Over")
        input("")
