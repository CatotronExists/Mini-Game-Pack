import time
import random 
import math

income_timer = 0
income_timer_start = time.time()
cases = 0
base_income = 1
total_item_value = 0
cases_open = 0
shop_open = 0
menu = 0
cost = 0
purchase_processing = 0
purchase_menu = 0
total_cost = 0
purchase_type = 0
max_case_cost = 0
purchase_amount = 0
loading_screen_text = ["Restocking the Store...", "Valuating Items...", "Prepairing Cases", "Praying to RNGesus", "Prepairing Dice", "", ]
case_numbers = [0,         1,          2,         3,                 4,              5,            6,           7,       8,       9,         10]
case_types = ["N/A", "Soggy Paper", "Paper", "Cardboard", "Reinforced Cardboard", "Wooden", "Stained Wooden", "Clay", "Brick", "Stone", "Refined Stone", ] #add more
case_prices = [0,        10]
#################################
# LOOT TABLES #
# sp <-- case name | case <-- case | lt <-- loot table | ch <-- chance | value <-- Value of item
sp_case_lt = ["Paper Mush", "Wet Paperball", "Damp Paper", "Paper Mache", "Wet Sticky Note", "Liquid Paper"]
sp_case_lt_ch = ["65%", "20%", "5%", "5%", "4%", "1%"]
sp_case_lt_value = ["1", "2.5", "5", "5", "7", "15"]

vaild_actions = ["shop", "Shop", "Inventory", "inventory", "inv", "i", "Item_List", "item_list", "il", "Case_List", "case_list", "cl",]
vaild_shop_options = ["1", "cases", "Cases", "2", "Upgrades", "upgrades", "0", "Close", "close", "x"]
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
            income_timer = income_timer - 1 # removes 1 second from timer
            update_total_value() # Updates Total Item Value
            balance += base_income + (total_item_value/2) # Balance updated
            balance = int(balance)

def update_total_value():
    global total_item_value 

def return_to_main_menu():
    global menu, shop_open, case_menu, purchase_menu, purchase_processing
    menu = shop_open = case_menu = purchase_menu = 0
    purchase_processing = 1
    time.sleep(1)
    income()   

while game_play == 0:
    while menu == 0: # Main Menu
        action_select = 0
        while action_select == 0:
            income()
            print("\n--------------------------------------------------------------------")
            print("Case Opening Simulator                                        v0.0.2\n")
            action_select = input("1. Shop\n2. Cases (Soon)\n3. Inventory (Soon)\n-->> ")
            if action_select == "shop" or action_select == "Shop" or action_select == "s" or action_select == "1": # Shop Convert 
                menu = shop_open = 1
            else: # Invaild Return
                print("Invaild Option")
                action_select = 0
                time.sleep(1)
    while menu == 1: # Shop Menu
        while shop_open == 1:
            income() 
            print("--------------------------------------------------------------------")
            print("Welcome to the shop!                          Current Balance: $"+str(balance))
            print("\n1. Cases")
            print("2. Upgrades (Coming Soon)")
            print("3. (Coming Soon)")
            print("0. Close\n")
            shop_option = input("-->> ")
            if shop_option == "1" or shop_option == "Cases" or shop_option == "cases" or shop_option == "c": # Cases Convert
                case_menu = 1
                shop_open = 0
            elif shop_option == "2" or shop_option == "Upgrades" or shop_option == "upgrades" or shop_option == "u": # Upgrade Convert
                print("Upgrades Coming Soon") 
                time.sleep(1)
            elif shop_option == "0" or shop_option == "Close" or shop_option == "close" or shop_option == "x": # Close Shop
                shop_open = menu = 0
            else:  # Shop Invaild
                shop_option = 0
                print("Invaild Option")
                time.sleep(1)
        while(case_menu == 1): # Page 1
            income()
            case_menu1_choice = 0
            print("--------------------------------------------------------------------")
            print("Case Shop                                      Current Balance: $"+str(balance))
            print("1. Soggy Paper Case [$10]")
            print("2. Paper Case [$100] (coming soon)")
            print("3. Cardboard Case [$250] (coming soon)")
            print("4. Reinforced Cardboard Case [$1000] (coming soon)")
            print("5. Wooden Case [$2.5k] (coming soon)")
            print("6. Page 2")
            print("0. Exit ")
            print("                                                               Page "+str(case_menu)+"/1") # Update page number when adding more
            while case_menu1_choice == 0: # Loop until Vaild Choice
                case_menu1_choice = int(input("-->> "))
                if case_menu1_choice in case_numbers:
                    case_choice = case_menu1_choice
                    if case_choice == 0: # Close
                        case_menu1_choice = -1
                        case_menu = 0
                        shop_open = 1
                    elif case_choice > 1: # Cases that dont exist yet
                        print("This Case has not been released yet!")
                        case_menu1_choice = 0
                    elif case_choice == 1: # Opens Purchase Menu
                        print(case_types[case_choice])
                        purchase_menu = 1
                    else: 
                        print("Error")
                else:
                    print("Invaild Option")
                    time.sleep(1)
                    case_menu1_choice = 0
            while purchase_menu == 1:
                income()             
                cost = case_prices[case_choice]
                max_case_purchase = (balance/cost)
                max_case_purchase = int(max_case_purchase)
                max_case_cost = max_case_purchase*cost
                math.floor(max_case_cost)
                print(max_case_cost)
                purchase_processing = 0
                while purchase_type == 0:
                    print("--------------------------------------------------------------------\nPurchase "+str(case_types[case_choice])+"                     Current Balance: $"+str(balance))
                    print("\nYou can purchase a max of "+str(max_case_purchase)+" "+str(case_types[case_choice])+" Cases")
                    purchase_type = input("Purchase Max (m) [$"+str(max_case_cost) +"] or Purchase 1 (1) [$"+str(case_prices[case_choice])+"]\n-->> ") # add custom purchase amounts
                    if purchase_type == "1": purchase_amount = 1 # One Case
                    elif purchase_type == "m": purchase_amount = max_case_purchase # Max Cases
                    else:
                        print("Invaild Option")
                        time.sleep(1)
                        purchase_type = 0

                while purchase_processing == 0:
                    total_cost = cost * purchase_amount 
                    if balance > total_cost:
                        balance =- total_cost
                        print("You Purchased "+str(purchase_amount)+" "+str(case_types[case_choice])+" Cases for $"+str(total_cost))
                        base_income += purchase_amount
                        return_to_main_menu()
                    else: 
                        print("You dont have enough money")
                        return_to_main_menu()
