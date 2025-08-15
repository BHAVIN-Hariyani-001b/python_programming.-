# print to 1 to 100
# ****** while loop  ******

# i = 1
# while i < 6:
#     print(i,"bhavin")
#     i += 1

# print even odd number between 1 to 10 using while loop

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#     i += 1

# while loop use to BREAK keyword

# i = 1
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1


# ****** while loop useing ELSE statement ******** 
# With the else statement we can run a block of code once when the condition no longer is true:

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("Loop is end")


# while loop is use to in list item print **

# a = ["bhavin",1,43,"anand",False,None,"hariyani",12.43,True]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1 


# ****** for loop  *******
# use to range(start,end,step)

# for i in range(10):
#     print(i,end=" ")

# print(end="\n")

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i,end=" ")

# Even strings are iterable objects, they contain a sequence of characters:
# for i in "BHAVIN":
#     print(i)

# for loop use to else 
# for i in range(5):
#     print(i,end=" ")
# else:
#     print("Loop is end")


#  ********* break **********

# With the break statement we can stop the loop before it has looped through all the items:

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# ****** continue ********

# With the continue statement we can stop the current iteration of the loop, and continue with the next: and skip to current step 
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# ****** pass ********

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# pass is a null statement in python. 
# It instructs to “do nothing”. 
# for i in [1,2,3,4]:
#     pass

# HOW TO RUN INFINITY RUN FOR LOOP
# AND BREAK TO USE (Ctrl+C)

from itertools import count
for i in count():
    print(i)