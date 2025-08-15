tupleData = ("bhavin","hariyani") # tuple is imutable like string and you can no change value 
print(tupleData)
print(type(tupleData))

# you can create empty tuple
print(type(()))
print(type(tuple()))

# print tuple 
print(tupleData[1]) # it is use to like list 
print(tupleData[::-1])  # and ### use to all slicing methos use and nagative index is allow to in tuple 
print(tupleData[-1])

# use to loop and allow to while and for loop use and check to condition and if else use 
# and access to index use 
for i in tupleData:
    print(i,end="*")
print(end="\n")

i = 0
while i < len(tupleData):
    print(tupleData[i],end="\t")
    i += 1
print(end="\n")

# tuple value change
# tupleData[1] = 32  # you can not change value and tuple is immutable 
# print(tupleData)

# function *********
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) # len is check to length of tuple
print(mytuple.count("apple")) # count is count value to pass 
print(mytuple.index("cherry")) # it is index find and return first index


# update tuple ******** 

# tuple is not change value it is immutable like string
# you can tuple value change to  and convert to list and change value and reconvert to tuple like this 👇
# and allow list function use to to in tuple and first convert to list and apply changeing 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "bhavin"
x = tuple(y)
print(x)

# append value
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


# concatination use to tuple join 
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# The del keyword can delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) 



# unpack  *** like java script destructuring 

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)