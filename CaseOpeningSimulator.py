import time
import random 

income_timer = 0
income_timer_start = time.time()
cases = 0
base_income = 1
total_item_value = 3
cases_open = 0
shop_open = 0
menu = 0
cost = 0
total_cost = 0
loading_screen_text = ["Restocking the Store...", "Valuating Items...", "Prepairing Cases", "Praying to RNGesus", "Prepairing Dice", "", ]
case_types = ["N/A", "Soggy Paper", "Paper", "Cardboard", "Reinforced Cardboard", "Wooden", "Stained Wooden", "Clay", "Brick", "Stone", "Refined Stone", ] #add more
#################################
# LOOT TABLES #
# sp <-- case name | case <-- case | lt <-- loot table | ch <-- chance | value <-- Value of item
sp_case_lt = ["Paper Mush", "Wet Paperball", "Damp Paper", "Paper Mache", "Wet Sticky Note", "Liquid Paper"]
sp_case_lt_ch = ["65%", "20%", "5%", "5%", "4%", "1%"]
sp_case_lt_value = ["1", "2.5", "5", "5", "7", "15"]

vaild_actions = ["shop", "Shop", "Inventory", "inventory", "inv", "i", "Item_List", "item_list", "il", "Case_List", "case_list", "cl",]
vaild_shop_options = ["1", "cases", "Cases", "2", "Upgrades", "upgrades", "3", "4", "Close", "close"]
inventory = []
game_play = 0
balance = 0 
action_select = 0
shop_status = 0 # 0 = closed, 1 = open
shop_option = 0
case_menu = 0 # 0 = not opened, 1 = open (pg 1), 2 = open (pg 2)
case_menu1_vaild = ["1", "Soggy Paper", "soggy paper", "2", "Paper", "paper", "3", "Cardboard", "cardboard", "4", "Reinforced Cardboard", "reinforced cardboard", "5", "Wooden", "wooden", "6", "Page 2", "page 2", "pg 2", "7", "Exit", "exit", ]
case_menu1_choice = 0
case_choice = -1
purchase_option = 0
max_case_purchase = 0

def income():
    global balance, base_income, income_timer, income_timer_end, income_timer_start
    income_timer_end = time.time() # Timer stops to | calculate how long it has been since last income
    income_timer = income_timer_end - income_timer_start # | Calculate "" ""
    if income_timer > 1:
        while income_timer > 1:
            income_timer_start = time.time() # Begins counting since last income
            print("Current Balance: $"+str(balance))
            print(int(income_timer))
            income_timer = income_timer - 1 # removes 1 second from timer
            update_total_value() # Updates Total Item Value
            balance += base_income + (total_item_value/2) # Balance updated

def update_total_value():
    global total_item_value 

while(game_play == 0):
    while menu == 0: # Main Menu
        print("--------------------------------------------------------------------")
        print("Case Opening Simulator                         [First Build]  v0.0.1")
        print("Only a shop for now!")
        action_select = input("1. Shop\n2. Cases (Soon)\n3. Inventory (Soon)\n-->> ")
    
    if(action_select in vaild_actions):
        if(action_select == "shop" or action_select == "Shop" or action_select == "s" or action_select == "1"):
            action_select = 0
            shop_open = 1
            while menu == 1:
                while(shop_open == 1): 
                    print("--------------------------------------------------------------------")
                    print("Welcome to the shop!                          Current Balance: $"+str(balance))
                    print("\n1. Cases")
                    print("2. Upgrades (Coming Soon)")
                    print("3. (Coming Soon)")
                    print("4. Close\n")
                    shop_option = input("-->> ")
                    if(shop_option == "1" or shop_option == "cases" or shop_option == "Cases" or shop_option == "c"): # Cases Menu
                        case_menu = 1
                        while(case_menu == 1): # Page 1
                            print("--------------------------------------------------------------------")
                            print("Case Shop                                      Current Balance: $"+str(balance))
                            print("1. Soggy Paper Case [$10]")
                            print("2. Paper Case [$100] (coming soon)")
                            print("3. Cardboard Case [$250] (coming soon)")
                            print("4. Reinforced Cardboard Case [$1000] (coming soon)")
                            print("5. Wooden Case [$2.5k] (coming soon)")
                            print("6. Page 2")
                            print("7. Exit")
                            print("                                                               Page "+str(case_menu)+"/1") # Update page number when adding more
                            case_menu1_choice = input("-->> ")
                            while(case_menu1_choice == "1" or case_menu1_choice == "Soggy Paper" or case_menu1_choice == "soggy paper" or case_menu1_choice == "sp"): # will be made so this "if" will be for all cases
                                case_choice = 1
                                # Soggy Paper Purchase menu
                                cost = 10
                                max_case_purchase = (balance/10)
                                max_case_purchase = int(max_case_purchase) 
                                print("Purchase Soggy Paper Case                                              Current Balance: $"+str(balance))
                                print("\nYou can purchase a max of "+str(max_case_purchase)+" "+str(case_types[case_choice])+" Cases")
                                purchase_type = input("Purchase Max (Soon) or Purchase 1 (1)\n-->> ") # add custom purchase amounts
                                if purchase_type == "1":
                                    total_cost = cost * 1 
                                    if balance > total_cost:
                                        balance =- total_cost
                                        print("You Purchased 1 Soggy Paper Case")
                                    else: 
                                        print("You dont have enough money")
        
                    elif(case_menu1_choice not in case_menu1_vaild): print("Invaild Option")

                    if(shop_option == "2" or "Upgrades" or "upgrades"):
                        # Add Upgrade Menu & System
                        print("Upgrades Coming Soon")
                    if(shop_option == "3"): print("Inventory Coming Soon")       
                    if(shop_option == "4" or "Close" or "close"): shop_open = 0       
                if(shop_option not in vaild_shop_options): print("Invaild Option")
    if(action_select not in vaild_actions): print("Invaild Option")
