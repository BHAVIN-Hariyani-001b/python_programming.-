# a = 23 # a is global variable it is use to in this code  
# def fun():
#     a = 3 # local variable in this function
#     print(a) # print local variable
# fun()
# print(a)

# a = 23 # a is global variable it is use to in this code  
# def fun():
#     print(a) # print global varibel
# fun()
# print(a)

a = 12
def fun():
    global a # global variable access in this function
    a = 4 # global variable change value
    print(a)
fun()
print(a)