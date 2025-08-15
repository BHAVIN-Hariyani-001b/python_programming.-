l = [1,2,3,4,5]
square = lambda x : x * x
#  use map function and lambda function
sqlist = map(square,l)
print(list(sqlist))


# filter
def even(n):
    if n % 2 == 0:
        return True
    return False
onlyList = filter(even,l)
print(list(onlyList))

# reduse
# reduse function is import to functools
from functools import reduce

def sum(a,b):
    return a+b

print(reduce(sum,l)) # call the function and pass to list and function