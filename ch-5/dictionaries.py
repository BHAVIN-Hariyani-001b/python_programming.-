# dictionari is mutable and you can change vlaue 
marks = {
    "bhavin":100,
    "harry":89,
    "abhay":98,
    "anand":76
}

print(marks) # print all dictionaries
print(type(marks)) # type of dictionaries
print(marks.keys()) # print dictionaries key in array from

# print to spacific value
print(marks['bhavin'])
print(marks['harry'])

# print length of dictionaries
print(len(marks))


# NOTE dictinaris is store to all value like bool,int,char,string,list,set,tuple etc.....
nameOfColor = {
    "color":"red",
    "setColor": ("black","blue","green"),
    "listColor":["pink","yellow","skyblue"],
    "isColoer":False,
    "bhavinBagColor":"balck",
    "anandPhoneColor":"blue",
}

# print(nameOfColor['listColor'][1])
print(nameOfColor)
print(nameOfColor['listColor'])
print(nameOfColor["setColor"])
# print(nameOfColor["setColor"][0]) 
print(nameOfColor["color"])

# dict keyword use to create dictionaries
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#There is also a method called get() that will give you the same result: like => nameOfColor["setColor"] <== same but pass anvalid value and return error
x = nameOfColor.get("setColor") # it is return value and not value stored in dict and return none  // that is not error it return none
print(x)
# The keys() method will return a list of all the keys in the dictionary.
print(nameOfColor.keys())


#change value in dictionary
nameOfColor["color"] = "white" 
print(nameOfColor['color'])

#The values() method will return a list of all the values in the dictionary.
print(nameOfColor.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(nameOfColor.items())

# use to if else with dictionaries
if "color" in nameOfColor:
    print("yes 'color' is available in dictionary")
else:
    print("no 'color is not available in dictionary'")

# print to int loop

for i in nameOfColor:
    print(f"{i} : {nameOfColor[i]}")


# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Update the "year" of the car by using the update() method:

# add new item **********

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# this is pass to new key and it is add to key and value
thisdict["MustangColor"] = "balck"
print(thisdict)
# The setdefault() method returns the value of the item with the specified key.
thisdict.setdefault("ModalType", "Bronco")
print(thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
# Add a color item to the dictionary by using the update() method:
thisdict.update({"type":"vihicals"})
print(thisdict)

#remove ************

# The pop() method removes the item with the specified key name:
thisdict.pop("type")
print(thisdict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:
del thisdict["year"]
print(thisdict)

#   The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# loop use to **************

animal_dict = {
    1: "Lion",
    2: "Tiger",
    3: "Elephant",
    4: "Zebra",
    5: "Giraffe"
}

for i in animal_dict:
    print(f"{i} :{animal_dict[i]}")
    # i is store to key value from dictionary 
    # i use to print animal_name


# you can also use the values() method to return values of a dictionary:
for i in animal_dict.values():
    print(i)

# You can use the keys() method to return the keys of a dictionary:
for i in animal_dict.keys():
    print(i)

# Loop through both keys and values, by using the items() method: and item method is return value in tuple format
for i in animal_dict.items():
    print(i)

# copy dictionaries *************

# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries **************

# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)


# use to for loop  in nested dictionary
# i is store to key of inner object and obj is store in inert object and use to item() function
for i,obj in myfamily.items():
    print(i)
    print(obj)
