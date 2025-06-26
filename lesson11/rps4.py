import sys
import random
from enum import Enum

game_count= 0

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
    
    def decide_winner(player, computer):
        if player==1 and computer==3:
           return "🎊congratulations, you won"
        elif player==2 and computer==1:
           return "🎊congratulations, you won "
        elif player==3 and computer==2:
           return "🎊congratulations, you won"
        elif player==computer:
           return "Tie game"
        else:
           return "😞computer wins"
       
       
    game_result= decide_winner(player,computer)
    print(game_result)        
        
    global game_count
    game_count+=1
    
    print("\nGame count"  + str(game_count))
    
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

