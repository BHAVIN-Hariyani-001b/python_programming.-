# def square(n):
#     return n * n

# lambda function ***

# find square of n
square = lambda n : n * n 
print(square(5))

# sum of tow number 
sum = lambda a,b : a + b
print(sum(10,5))

# use lambda in function 
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))





