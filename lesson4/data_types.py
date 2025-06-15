# string data type

# # literal assignment
first="akshat"
last="chauhan"
# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

# print('')

# # constructor function
# pizza= str("margerita")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))


#concatination adding two strings together
fullname= first + " " + last
print(fullname)
print("")
fullname+="!"
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement= "i like rock music from the " + decade + "s."
print (statement)

#multiple line
multiple_line= '''
Hey how are you?
                    all good?
okay cool
'''
print(multiple_line)

#escaping special characters
sentence= 'I\'m back at work! \t hey\n okay cool'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiple_line.title()) #caps all first letter
print(multiple_line.replace("good","okay-bye"))
print(multiple_line)

print(len(multiple_line))
multiple_line+="                                       "
multiple_line="               " + multiple_line
print(len(multiple_line))

print(len(multiple_line.strip()))  #to remove white spaces
print(len(multiple_line.lstrip()))  #to remove white spaces from left side
print(len(multiple_line.rstrip()))  #to remove white spaces from right side
print("")

#build a meanu
title="menu".upper()
print(title.center(20, "="))
#print("coffee".ljust(16,"."))
print("coffee".ljust(16,".") + "$1".rjust(4))
print("muffin".ljust(16,".") + "$3".rjust(4))
print("cheesecake".ljust(16,".") + "$5".rjust(4))


#string index value (index starts from 0)
print(first[1]) # prints second value cuz indexing starts from 0
print(first[-1]) # prints last letter
print(first[1:4]) # value given here won't be printed i.e value b/w these will be printed
print(first[1:-1]) 
print(first[1:])

#some method returns bolean data
print(first.startswith("a"))
print(first.endswith("z"))

#bolean data types:
myvalue= True #should start with capital T
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numeric data types
price = 100
best_price= int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa= 3.28
y = float(1.14)
print(type(gpa))

#complex type
comp_value= 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#built-in functions for numbers
print(abs(gpa))
print(round(gpa)) #will round to nearest integer
print(round(gpa,1)) #will round to nearest decimal place we specify

import math

print(math.log (2))
print(math.pi)

#type print(math.) and check for anything like for sqrt(64) etc etc
#print math is a built in data type here, so we can use it anywhere!




