# #loops in python
value=1
# while value<10:
#     print(value)
#     value+=1

# print("")
# value=1
# while value<=10:
#     print(value)
#     if value ==5:
#         break
#     value+=1
    
# value=1
# while value<=10:
#     value+=1
#     if value ==5:
#         continue #does not prints 5
#     print(value)
# else:
#     print("value is now equal to"+str(value))

# names= ["Dave", "Sarah", "John"]
# for x in names: #CAn write anything instead of x
#     print(x)

# for x in "MISSISSIPPI":
#     print(x)

# for x in names:
#     if x == "Sarah":
#         break
#     print(x)
# print("")
# for x in names:
#     if x == "Sarah":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2,4):
#     print(x)
# for x in range(0,100,5): #start from 0 till 100 and increment each number from 5
#     print(x)
# else:
#     print("Glad that\'s over!")

names= ["Dave", "Sarah", "John"]
actions=["codes","eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name+" "+action+".")

# for action in actions:
#     for name in names:
#         print(name+" "+action+".")

for action in actions:
    for name in names:
        print(name+" "+action+".")


