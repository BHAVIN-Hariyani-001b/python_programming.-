age = int(input("enter your age : "))
# if
if age > 18:
    print("you are vote now")

# if else
if age > 18:
    print("you are vote now")
else:
    print("you are not vote")


# else if  // else if ladder
if age > 18:
    print("you are vote now")
elif age < 12:
    print("you are child")
elif age > 60:
    print("you are retire")
elif age > 100:
    print("you age is not valid")
else:
    print("you are not vote")

# Short Hand If
a = 13
b = 11
if a > b: print("a is big")

# Short Hand If ... Else
print("a is big") if a > b else print("b is big")

# short hand if else if else
a,b = 10,10
print("a is big") if a > b else print("a and b are equal") if a == b else print("b is big")

# same to like *******
if a > b:
    print("a is big")
elif a == b:
    print("a and b are equal")
else:
    print("b is big")


# use to logical oprator and conditional opreator 
a,b = 10,10

# The and keyword is a logical operator, and is used to combine conditional statements:
# use to AND
if a > b and a == b:
    print("hello")
else:
    print("by")

# The or keyword is a logical operator, and is used to combine conditional statements:
# use to OR
if a > b or a == b:
    print("hello")
else:
    print("by")

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# use to NOT
if not True:
    print("true")
else: 
    print("false")

# Nested If *****
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass