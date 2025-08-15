# List *********
# list is store to multiple value in sigale varible

# friends = ["bhavin","hemal","bhaval",1,34,54,False,43.54]
# print(friends)
# print(friends[0])
# print(friends[-1])

# friends[0] = "hariyani"  # list is mutable it is change 
# print(friends) # change and show value
# print(type(friends))
# print(len(friends))

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# funciton ******

# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# The remove() method removes the specified item.
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # if not print to value and if is list remove 

# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# use to slicing list *********

# data = ["bhaivn","anand","sagar","abhay","sagil"]
# print(data[:])
# print(data[:-1]) # remove last index
# print(data[1:]) # remove first index
# print(data[::-1]) # reverse list
# print(data[1::])
# print(data[1:4])
# print(data[-5:-1])
# print(data[0::2]) # it is skip index


# use to loop and print list item
data = ["apple", "banana", "cherry"] 
for i in data:
    print(i,end=",")
print(end="\n")

# and index number use to print list data
for i in range(len(data)):
    print(data[i],end=",")
print(end="\n")

# use while loop and print list data
i = 0
while i < len(data):
    print(data[i],end="\t")
    i = i + 1
print(end="\n")

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:
# a = [print(i,end="_") for i in data]

# Python - List Comprehension ************
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newItem = []
for i in fruits:
    if "a" in i:
        newItem.append(i)
print(newItem)

# sort hand
# The Syntax
#### newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
newItem = [i for i in fruits if "a" in i]
print(newItem)

newItem = [i for i in fruits if i != "apple"]
print(newItem)


# The condition is optional and can be omitted: **
newItem = [i for i in fruits]
print(newItem)

range_ = [i for i in range(10)]
print(range_)

even = [i for i in range(10) if i % 2 == 0]
print(even)

even = [i for i in range(10) if i % 2 != 0]
print(even)

upperChar = [i.upper() for i in fruits]
print(upperChar)

# ****** there are same and not a diffrent (1 and 2)
# 1 
newItem = ['HELLO' for i in fruits] 
print(newItem)
# 2 
newItem = []
for i in fruits:
    newItem.append('bhavin')
print(newItem)

# ** if else in short and loop
newItem = [i if i != "banana" else "bhavin" for i in fruits]
print(newItem)

# use to if else item is present to in this list
# if "bhaivn" in data:
#     print("bhavin is data present to data list")
# else:
#     print("bhavin is data not present to data list")




# ** sort list *********


# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort to acending order
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# copy *******

# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist.append("bhavin")
print(mylist)
print(thislist)


# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist.append("bhavin")
print(mylist)
print(thislist)


# Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
mylist.append("bhavin")
print(mylist)
print(thislist)


# JOIN  ******* list

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)


# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# List Methods ********

# count() ***
# Syntax   
# list.count(value)
# The count() method returns the number of elements with the specified value.
# Required. Any type (string, number, list, tuple, etc.). The value to search for. **
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)


# index() ***
# Syntax
# list.index(elmnt, start, end)
# elmnt	= Required. Any type (string, number, list, etc.). The element to search for
# start	= Optional. A number representing where to start the search
# end =	Optional. A number representing where to end the search
# The index() method returns the position at the first occurrence of the specified value.

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

