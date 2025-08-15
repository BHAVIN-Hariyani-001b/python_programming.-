# 1
    # complited

# 2 
# name = input("Enter your name : ")
# marks = input("Enter your marks : ")
# phone = input("Enter your phone : ")

# print("my name is {} and my 12 exam mark is {} and my phone number is  {}".format(name,marks,phone))


# 3 
# n = 7
# l = [str(i*n) for i in range(1,11)]

# tableStr = "\n".join(l)
# print(tableStr)


# 4

# data = [1,2,5,10,1,5,15,35,55,100,90]

# def divisible5(n):
#     if n % 5 == 0:
#         return True
#     return False

# f = list(filter(divisible5,data))
# print(f)


# 5

from functools import reduce

# it is valid qestion
l = [1,2,3,4,5,1,3,6,7,2,8,10]
def maxNum(a,b):
    if a > b:
        return a
    return b
print(reduce(maxNum,l))

# OR

# def maxNum(n):
#     maxN = 0
#     for i in n:
#         if i > maxN:
#             maxN = i
#     return maxN
            
# print(maxNum(l))

# OR

# print(max(l))