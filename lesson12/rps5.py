import sys
import random
from enum import Enum

def rps():
    game_count= 0
    player_wins = 0
    computer_wins = 0
    

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
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
            nonlocal player_wins
            nonlocal computer_wins
            
            if player==1 and computer==3:
                player_wins+=1
                return "🎊congratulations, you won"
            elif player==2 and computer==1:
                player_wins+=1
                return "🎊congratulations, you won "
            elif player==3 and computer==2:
                player_wins+=1
                return "🎊congratulations, you won"
            elif player==computer:
                return "Tie game"
            else:
                computer_wins+=1
                return "😞computer wins"
        
        
        game_result= decide_winner(player,computer)
        print(game_result)        
            
        nonlocal game_count
        game_count+=1
        
        print("\nGame count"  + str(game_count))
        print("\nplayer count:"  + str(player_wins))
        print("\ncomputer count:"  + str(computer_wins))
        
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
    
    return play_rps

play=rps()
play()
