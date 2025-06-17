#dictionaries
band= {
    "vocals":"plant",
    "guitar": "page"
}
band2=dict(vocals="plants", guitar="page")
print(band)
print(band2)

#access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())
print(band.values())
print("guitar" in band)
print("telephone" in band)

band.update({"bass":"jpj"})
print(band)

band["drums"]="Bonham"
print(band)

print(band.popitem()) #tupule
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaries
# band2=band #creates a refrence i.e both refers to the same place in the memory or dictionary
# print("bad copy")
# print(band2)
# print(band)

# band2["drums"]="Dave"
# print(band)

band2= band.copy()
band2["drums"]="Dave"
print("good copy!")
print(band)
print(band2)

#using dict constructor function
band3= dict(band)
print("goodcopy")
print(band3)

#nested dictionary
member1 = {
    "name": "Jess",
    "instrument":"vocals"
}
member2= {
    "name":"Page",
    "instrument": "guitar"
}
member3= {
    "name":"Rock",
    "instrument" : "piano"
}

band4={
    "member1": member1,
    "member2": member2,
    "member3": member3
}
print(band4)
print(band4["member1"]["name"])
# band. to see others available

#sets
nums={ 1, 2, 3, 4}
nums2= set((1,2,5,6))
print(nums)
print(nums2)
#it doesn;t allowes duplicates
nums3={1,2,2,3,3,4}
print(nums3)
print(len(nums3))
#you cannot refer to an element in set with an index position or a key
nums3.add(8)
print(nums3)
#you can use update using tuples, list, and dictionaries too
