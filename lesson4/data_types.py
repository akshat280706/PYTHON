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




