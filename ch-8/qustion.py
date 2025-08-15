# 1 
# def greatestNum(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# print(greatestNum(2,3,4))

# def greatestNum(*a):
#     return max(a)
# print(greatestNum(2,3,4))

# 2
# def CelsiusToFahrenheit(c):
#     f = (c * (9/5)) + 32
#     return f    

# print(CelsiusToFahrenheit(int(input("Enter your Number"))))

# def FahrenheitTOCelsius(f):
#     c =  (f - 32) * (5 / 9)
#     return c
# print(FahrenheitTOCelsius(int(input("Enter your Number"))))

# 3

# def printNewLine():
#     print("B",end="")
#     print("H",end="")
#     print("A",end="")
#     print("V",end="")
#     print("I",end="")
#     print("N",end="")
# printNewLine()

# 4

# def sum(n):
#     if n <= 0: return 0
#     if n == 1: return 1
#     return n + sum(n-1)
# print(sum(5))


'''
and it like to >>>>> stack <<<<<

sum(5)
= 5 + sum(4)
= 5 + (4 + sum(3))
= 5 + (4 + (3 + sum(2)))
= 5 + (4 + (3 + (2 + sum(1))))
= 5 + 4 + 3 + 2 + 1
= 15

---------------

sum(5)
-> 5 + sum(4)
      -> 4 + sum(3)
            -> 3 + sum(2)
                  -> 2 + sum(1)
                        -> 1 (base case)

Now return:
1 → 2+1 → 3+3 → 4+6 → 5+10 = 15

---------------

sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 + .... n
'''

# return keyword use ***
    # - exit function
    # - value return

# 5 pattern in use to recurssion
# def pattern(n):
#     if n == 0: 
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(5)


#6 
# def inch_to_cms(inch):
#     return inch * 2.54
# print(inch_to_cms(int(input("Enter you inches : "))))

# 7
# l = ["Bhavin","anand","a","aman","abhay"]

# def remove(l,word):
#       n = []
#       for i in l:
#             if i != word:
#                   n.append(i.strip(word))
#       return n
# print(remove(l,"abc"))

#8

# def table(n):
#     for i in range(1,11):
#       print(f"{n} x {i} = {n * i}")
# table(int(input("Enter your table number : ")))


