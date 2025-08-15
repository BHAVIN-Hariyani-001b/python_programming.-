# set is not any value repit it is 
# and set is mutable 
# and oreder is not maintain
# store to multiple value
# can not assess in index
# set is callection of multpile value
# set is not work slicing

a = {"bhavin","anand","hariyani"}
print(a)


emptySET = set() # empty set create 
print(type(emptySET))


# function ***********
num = {1,2,3,4,"bhaivn"}
print(num)

print(len(num)) # lenght 
num.add("anand hariyani") # add() function is add to new value
print(num)

# To remove an item in a set, use the remove(), or the discard() method.
num.remove(2)       # Raises error if not found
num.discard(3)      # No error if not found
print(num)

num.pop() # pop use to delete rendome  value
print(num)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)


num.clear() # clear is remove all element in set

a = {1,2,3}
b = {3,4,5}
print(a.union(b)) # first set value print and second set value match and print match value print

print(a.intersection(b)) # same value return 
print(a.difference(b)) # diffrence value return in first set

print(a.symmetric_difference(b)) # it is use to print uniqu value two set

a = {a for a in range(5)} # Comprehension use to set
print(a)

# it is by defualt unique value return 
a = {1,1,2,3,4,5,3}
print(a)
unique = set(a)
print(unique)

copy = a.copy() # copy value and store to new variable
print(copy)

a = {1, 2}
b = {1, 2, 3}
a.issubset(b)   # True
b.issuperset(a) # True


#update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# and  update also use to join tow set and tuple,list and dictionaries
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# True and 1 is considered the same value:
# False and 0 is considered the same value:
# and not return duplicat value return
thisset = {"apple", "banana", "cherry", True, 1, 2,False,0}
print(thisset)

# use to loop
thisset = {"apple", "banana", "cherry"}

for i in thisset:
    print(i,end="\t")
print(end="\n")

print("apple" in thisset) # in is like to {=}
print("apple" not in thisset) # not in is like {!=}

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)


# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)