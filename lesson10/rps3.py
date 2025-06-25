import sys
import random
from enum import Enum

def play_rps():
    
    class RPS(Enum):
        Rock= 1
        Paper= 2
        Scissors= 3

    player_choice=input("enter...\n1. For Rock\n2. For paper\n3. For Scissors:\n\n")
    
    if player_choice not in ["1","2","3"]:
        print("Invalid input, Choose Between 1,2,3")
        return play_rps

    player=int(player_choice)

    computer_choice= random.choice("123")
    computer= int(computer_choice)

    print("")

    print("you chose:" + str(RPS(player)).replace('RPS.','') + ".")
    print("computer chose:" + str(RPS(computer)).replace('RPS.','')+ ".")

    if player==1 and computer==3:
        print("🎊congratulations, you won")
    elif player==2 and computer==1:
        print("🎊congratulations, you won ")
    elif player==3 and computer==2:
        print("🎊congratulations, you won")
    elif player==computer:
        print("Tie game")
    else:
        print("😞computer wins")
    print("\nPlay again?")
    
    while True:
        playagain = input("\nPlay again\nY for Yes\nN for No\n\n")
        if playagain.lower() not in ["y","n"]:
            continue
        else:
            break
        

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("thank you for playing\n")
        sys.exit("BYE!!")

play_rps()

