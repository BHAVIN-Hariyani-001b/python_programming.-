# function

# Built in functions (Already present in python) **
#  like len(),print(),range(),count(),sum() 

# User defined functions (Defined by the user) **
#like to this 👇

# noramal function ******
# def hello():
#     print(" HELLO")
# hello()

# def goodDay():
#     print("GOOD DAY")
# goodDay()

# argument peramiter function ******
# find avg of number 
# def avgOfNum(*a): # Formal Parameter ## use to peramiter is work to like tuple and peramiter
#     # print(a)
#     return sum(a) / len(a)
# print(avgOfNum(10,20,30)) # pass to value  --  ## Actual Parameter and argument


# def avg(num):
#     l = [int(input("ENTER YOUR NUMBER : ")) for i in range(num)]
#     print(sum(l) / len(l))
# avg(3)


# defualt value function ******
# def name(name = "Bhavin"): # it is pass to value and print to pass value and not pass to value and defualt value print
#     print(name)
# name("anand")
# name()

#return value funtion ***
# def sum(a,b):
#     return a + b
# print(sum(3,5))


# pass keyword use ***
# def abc():
#     pass
#     # function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


# Positional-Only Arguments ***
# def fun(x,/,c,d):
#     print(x,c)
# # fun(x = 5,c = 4,d = 56)  <-- this is not ❌ valid to pass before \ backword shlash assing value and pass and after is normal work to pass value to like normal function 
# fun(4,c = 9,d = 0) # <-- this is valid ✔️


# Keyword only argument ***
# def myfun(*,a): # To specify that a function can have only keyword arguments, add *, before the arguments:
#     print(a)
# # myfun(4) # this is not valid ❌
# myfun(a = 4) # this is valid ✔️

# Combine Positional-Only and Keyword-Only ****
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
# my_function(5, 6, c = 7, d = 8)

# RECURSION FUNCTION ****

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# febonachi
# def feb(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return feb(n - 1) + feb(n - 2)

# for i in range(10):
#     print(feb(i))

# natural number 
# def nat(num):
#     if num <= 0: return 0
#     if num == 1: return 1
#     return num + nat(num - 1)
# print(nat(5))



# def myfunc():
#     """
#     This is a multi-line comment or docstring.
#     It's not used as a comment officially,
#     but Python ignores it if not assigned or used.
#     """
#     print("Hello")
# myfunc()