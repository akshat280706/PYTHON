users=['rock', 'dave', 'gray']
data=['rock', 41, True]
empty_list=[]

print("rock" in users)
print("head" in users)
print(users[0])
print(users[-1])
print(users[-2])
print(users[-3])
print(users.index('gray'))

print(users[0:2])

#to add
users.append('sarah')
print(users)
print(len(users))
# users.extend(['jimmy','jason'])
print(users)

users.insert(0,'bob')
print(users)

users[2:2]= ['eddie','alex']
print(users)

users.remove('bob')
print(users)

print(users.pop()) #prints last value
print(users)

del users[0] #would delete the value at 0 index(rock here)
print(users)

users+=['rock']
print(users)

users[0:1]=['corey']
print(users)

data.clear()
print(data)

#alphabetical
users.sort()
print(users)

#lowercase comes after uppercase
users+=['Jason']
users.sort()
print(users)#jason will come first here

users.sort(key=str.lower)#now jason is also alphabetically: make sure its the same data_type i.e all are string or etc like that else it won't work
print(users)

#reverse a list
nums=[4,42,78,1,92]
nums.reverse()
print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

#original list is not modified and is the same
print(sorted(nums, reverse=True))
print(nums)


#Tuples:
mytuple= tuple(('Dave', 42, True))
anothertuple= (2,4,7,8)
print(mytuple)
print(type(mytuple))
print(anothertuple)

#to add in a tuple
newlist= list(mytuple)
newlist.append('Neil')
newtuple=tuple(newlist)
print(newtuple)
