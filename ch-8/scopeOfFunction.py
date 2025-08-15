# LEGB in Action ***********

x = "global"  # Global variable

def outer():
    x = "enclosing"  # Enclosing variable
    
    def inner():
        x = "local"  # Local variable
        print("Inner:", x)  # Finds local x
    
    inner()
    print("Outer:", x)  # Finds enclosing x

outer()
print("Global:", x)  # Finds global x



# Accessing Global Variables in a Function ***********

count = 10  # Global

def modify():
    global count  # Use global variable instead of creating local
    count += 5

modify()
print(count)  # 15


# nonlocal is used in nested functions to modify a variable from the enclosing scope. *********

def outer():
    value = 10
    
    def inner():
        nonlocal value  # Modifies enclosing variable
        value += 5
    inner()
    print("Value in outer:", value)

outer()


# Built-in Scope Example **********
# print(len("Python"))  # len is a built-in function
