#GUESS THE NUMBER

import random
import pystyle
from pystyle import Colors, Colorate
import os
import time
import ctypes
global winstreak
winstreak = 0

class fg:
  black = "\u001b[30m"
  red = "\u001b[31m"
  green = "\u001b[32m"
  yellow = "\u001b[33m"
  blue = "\u001b[34m"
  magenta = "\u001b[35m"
  cyan = "\u001b[36m"
  white = "\u001b[37m"
  reset = "\u001b[0m"
def gen_number():
    return random.randint(0, 10000)
def game():
    global winstreak
    toGuess = gen_number()
    wonBanner = """

 __      __                          __       __                      __ 
|  \    /  \                        |  \  _  |  \                    |  \\
 \$$\  /  $$______   __    __       | $$ / \ | $$  ______   _______  | $$
  \$$\/  $$/      \ |  \  |  \      | $$/  $\| $$ /      \ |       \ | $$
   \$$  $$|  $$$$$$\| $$  | $$      | $$  $$$\ $$|  $$$$$$\| $$$$$$$\| $$
    \$$$$ | $$  | $$| $$  | $$      | $$ $$\$$\$$| $$  | $$| $$  | $$ \$$
    | $$  | $$__/ $$| $$__/ $$      | $$$$  \$$$$| $$__/ $$| $$  | $$ __ 
    | $$   \$$    $$ \$$    $$      | $$$    \$$$ \$$    $$| $$  | $$|  \\
     \$$    \$$$$$$   \$$$$$$        \$$      \$$  \$$$$$$  \$$   \$$ \$$
                                                                         
                                                                         
                                                                         

"""
    #print(toGuess) #debugging
    guess = input(Colorate.Horizontal(Colors.red_to_green, "Your Guess: ", True))
    while guess != toGuess:
        if int(guess) > toGuess:
            print(f"{fg.red}Lower!\n {fg.reset}")
            guess = input(Colorate.Horizontal(Colors.red_to_green, "Your Guess: ", True))
        elif int(guess) < toGuess:
            print(f"{fg.green}Higher! \n{fg.reset}")
            guess = input(Colorate.Horizontal(Colors.red_to_green, "Your Guess: ", True))
        if int(guess) == toGuess:
            winstreak += 1
            return print(f"{fg.yellow}{wonBanner}\n{fg.reset}")
    
def __main__():
    banner = f"""
    


  _    _ _       _                     _                            
 | |  | (_)     | |              ___  | |                           
 | |__| |_  __ _| |__   ___ _ __( _ ) | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__/ _ \/\ |    / _ \ \ /\ / / _ \ '__|      [WinStreak: {winstreak}]
 | |  | | | (_| | | | |  __/ | | (_>  < |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|  \___/\/______\___/ \_/\_/ \___|_|   
            __/ |                                                   
           |___/                                                    
                                                                                           
[1] Start the game!
[2] Quit
    """
    
    
    print(Colorate.Horizontal(Colors.red_to_green, banner, True))
    os.system('title Higher^&Lower ^| WinStreak: {}'.format(winstreak))
    choice = input(Colorate.Horizontal(Colors.red_to_green, "Select an option: ", True))
    c = int(choice)
    if c == 1:
        game()
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        __main__()
    if c == 2:
        print("Thanks for playing!")
        import sys
        sys.exit()

__main__()