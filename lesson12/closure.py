# #closure is a function having access to scope of its parents
# # function after the parent function has returned

# def parent_function(person):
#     coins=3
    
#     def play_game():
#         nonlocal coins
#         coins-=1
        
#         if coins>1:
#             print("\n" + person+ " has " + str(coins)+ " coins left")
#         elif coins ==1:
#             print("\n" + person+ " has " + str(coins)+ " coins left")
#         else:
#             print("\n" + person+ " is out of coins")
    
#     return play_game

# tommy=parent_function("Tommy")
# jenny=parent_function("jENNY")

# tommy()
# tommy()
# jenny()
# tommy()