# 1 
# t = int(input("Enter your 'table' number : "))
# for i in range(1,11):
#     print(f"{t} x {i} = {t*i}")

# 3
# t = int(input("Enter your 'table' number : "))
# i = 1
# while i < 11:
#     print(f"{t} x {i} = {t*i}")
#     i += 1


# 2

# l = [input("Enter your name : ") for i in range(5)]
# print(l)
# for i in l:
#     if i.startswith("s"):
#         print(f"Hello {i}")


# 3

# l = []
# while True:
#     userName = input("Enter your Name || and stop to useing 'exit' : ")
#     if "exit" == userName:
#         break
#     l.append(userName)
# print(l)

# 4 
# def prime(p):
#     if p <= 1:
#         return False   
#     for i in range(2,p//2):
#         if p % i == 0:
#             return False
#     return True

# result = "Prime" if prime(7) == True else "Not Prime"
# print(result)

# n = int((input("enter your number : ")))
# for i in range(2,n):
#     if n % i == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# 5
# n = int(input("Enter your number : "))
# sum = 0
# while n != 0:
#     sum += n
#     n -= 1
# print(sum)

# n = int(input("Enter your number : "))
# sum = 0
# i = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


# n = int(input("Enter your number : "))
# l = [i for i in range(n)]
# print(sum(l))


# 6 
# def factorial(n):
#     if n <= 1: return 1
#     fact = 1
#     for i in range(2,n+1):
#         fact *= i
#     return fact
# print(factorial(5))

# def factorial(n):
#     if n <= 1: return 1
#     return n * factorial(n - 1)
# print(factorial(3))

# n = int(input("Enter your Number : "))
# product = 1
# for i in range(2,n+1):
#     product *= i

# print(f"The factorial is {n} is {product}")

# 7 use to other

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(end=" ")

#     for j in range(i+1):
#         if i % 2 == 0:

#             # OR
#     # for j in range(i):
#             print("*",end=" ")
#     print(end="\n")

#---- output ----

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(n):
#     for j in range(i):
#         print(end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print(end="\n")

#---- output ---- 

# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# 7
# n = int(input("Enter your number : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

# 8

# n = 3
# for i in range(n):
#     for j in range(i,n):
#         print(end="")
#     for j in range(i+1):
#         print("*",end="")
#     print(end="\n")

# OR

# n = int(input("Enter your number : "))
# for i in range(1,n+1):
#     print(""*(n-i),end="")
#     print("*"*(i),end="")
#     print("")

# 9

# n = 3
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or i == n - 1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(end="\n")

# OR

# n = int(input("Enter your number : "))
# for i in range(1,n+1):
#     if i == 1 or i == n:
#         print("* "*n,end="")
#     else:
#         print("* ",end="")
#         print("  "*(n-2),end="")
#         print("* ",end="")
#     print("")
    
    
# 10

# t = int(input("Enter your 'table' select : "))
# for i in range(10,0,-1):
#     print(f"{t} x {i} = {t*i}")

# OR

# t = int(input("Enter your 'table' select : "))
# for i in range(1,11):
#     print(f"{t} x {11-i} = {t*(11-i)}")

# t = int(input("Enter your 'table' select : "))
# for i in range(1,11):
#     print(11-i)