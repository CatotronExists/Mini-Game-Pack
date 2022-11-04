from libraries import *
from globals import *
from config import *
from functions import *
def main_menu_ui():
    from MiniGamePack import page
    vaild = False
    while vaild == False:
        print("   _________________________")
        print("__/ Mini Game Pack     v0.3 \_________")
        print("                                      |")
        print("Guessing Game.................(1 / gg)|")
        print("Rock Paper Scissors..........(2 / rps)|")
        print("Loading Screen Simulator.....(3 / lss)|")
        print("???.............................(v0.5)|")
        print("???.................................()|")
        print("???.............................(V0.4)|")
        print("Page "+str(page)+" of 1                    < o >  |")
        print("______________________________________|")
        vaild = input("-->> ")
        if vaild in vaild_games:
            if vaild == "1" or vaild == "gg": game_selected = 1
            elif vaild == "2" or vaild == "rps": game_selected = 2
            elif vaild == "3" or vaild == "lss": game_selected = 3
        else: invaild()
