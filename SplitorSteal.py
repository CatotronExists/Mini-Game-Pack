import random
from random import randint as dice
import time
vaild = False
mode = 0
first = 0
player1_choice = 0 # Player 1 is also the player vs Computer
# player1_bal = 0 Soon
player2_choice = 0 # Player 2 is also the computer in (vs computer mode)
# player2_bal = 0 Soon
choice_list = ["na", "Split", "Steal"]

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
            print("\n" * 99)
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
            print("\n" * 99)
            vaild = True
        else: invaild()

print("Split or Steal\nA Game about predicting the other player's choice\nYou have two options in front of you, Split or Steal.\nThe rules are simple, If both players Split the money will get split\nBut if one player Steals they get all the money, If both players are to Steal neither get anything.")
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

if mode == "Computer":
    first = dice(1,2) # Decides who goes first
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
        print("Computer has chosen")
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
        print("You chose to..."+str(choice_list[player1_choice])+"")
        time.sleep(random.random())
        print("Computer chose to..."+str(choice_list[player2_choice])+"")
    
    if first == 2:
        print("Computer chose to..."+str(choice_list[player2_choice])+"")
        time.sleep(random.random())
        print("You chose to..."+str(choice_list[player1_choice])+"")

    time.sleep (0.4)
    if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Steal": # Both users said Steal
        print("\nBecause Both Players chose to Steal, Neither of you get anything.")
    if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Split": # Both users said Split 
        print("\nBoth Players Chose to Split, Both Player will recieve the same amount of Money") 
    if choice_list[player1_choice] == "Steal" and choice_list[player2_choice] == "Split": # P1 Stole from P2
        print("\nYou Stole all the Money from Computer")
    if choice_list[player2_choice] == "Steal" and choice_list[player1_choice] == "Split": # P2 Stole from P1
        print("\nComputer Stole all the Money from You")
            
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
        print("Player 1 chose to..."+str(choice_list[player1_choice])+"")
        time.sleep(random.random())
        print("Player 2 chose to..."+str(choice_list[player2_choice])+"")
    
    if first == 2:
        print("Player 2 chose to..."+str(choice_list[player2_choice])+"")
        time.sleep(random.random())
        print("Player 1 chose to..."+str(choice_list[player1_choice])+"")
    
    if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Steal": # Both users said Steal
        print("Because Both Players chose to Steal, Neither of you get anything.")
    if choice_list[player1_choice] == choice_list[player2_choice] and choice_list[player1_choice] == "Split": # Both users said Split 
        print("Both Players Chose to Split, Both Players will recieve the same amount of Money") 
    if choice_list[player1_choice] == "Steal" and choice_list[player2_choice] == "Split": # P1 Stole from P2
        print("Player 1 Stole all the Money from Player 2")
    if choice_list[player2_choice] == "Steal" and choice_list[player1_choice] == "Split": # P2 Stole from P1
        print("Player 2 Stole all the Money from Player 1")

print("Game Over")
