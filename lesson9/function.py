def hello():
    print("hello duniya!!") #will not print here, we will have to call the function

hello()# to call the function

def hello_world():
    print("bye")
hello_world()

# parameters are variables declared in a function's definition, 
# acting as placeholders for the values that will be passed in. 
# Arguments are the actual values passed to a function when it is called, 
# which then get assigned to the corresponding parameters.

# def sum(num1 , num2): #num1,num2 are parameters
#     print(num1+num2)
# sum(2,3) #these values are the arguments
# sum(1,7)
# sum(100,3)

def sum(num1,num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

def sum(num1,num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1+num2
total=sum(2)
print(total)

total=sum('a',3)
print(total)

# total=sum()
# print(total) #will give an error

total=sum(2,3)
print(total)


def multiple_item(*args):
    print(args)
    print(type(args))

multiple_item("dave","john","sarah","Rock")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Akshat", last="chauhan")
