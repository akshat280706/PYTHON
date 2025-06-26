# name="dave"

# def greeting(first_name):
#     color="blue"
#     print(name)
#     print(color)
#     print(first_name)
# greeting("JOHN")

name="dave"

# def greeting(name):
#     color="blue"
#     print(color)
#     print(name)
# greeting("JOHN")

    
# #we can call one fxn inside of the local scope of another function
# def another():
#     greeting("dave")
    
# another()

#we can also define functions inside of another functions
# def another(): #global scope
#     color="blue"
    
#     def greeting(name): #local scope
#         print(color)
#         print(name)
        
#     greeting("JOHN")
# another()
# greeting("JOHN") #will have to define inside the first function only else it would give an error

count=1
def another(): #global scope
    color="blue"
    count =2 
    #count+=1 would give an error, we can't modify here as we had created count globaly
    #instead we can write:
    #global count
    #count +=1
    print(count)
    
    def greeting(name): #local scope
        print(color)
        print(name)
        
    greeting("JOHN")
another()


