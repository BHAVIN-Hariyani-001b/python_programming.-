# try:
#     a = int(input("hey , enter number : "))
#     print(a)
# except Exception as e:
#     print(e)

# print("Thank you")

# specific ValueError ********
# try:
#     a = int(input("hey , enter number : "))
#     print(a)
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)

# print("Thank you")

# raise exception **********
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# if b == 0:
#     raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
# else:
#     print(f"The Division a/b {a/b}")



# try with else *****
# else body part run in run to try body and run else 
# and not run try and run is except and not run else part

# try:
#     a = int(input("Enter a number : "))
#     print(a)
# except Exception as e:
#     print(e)
# else:
#     print("Nothing went wrong")

# try with finally

# finally is use in most function and finally is always run and function use to return value and than after you can use to finally and finally is alwasy run 
# and not affect to return in finally and it is alwasy run 

def main():
    try:
        a = int(input("enter your number : "))
        print(a)
        return
    except Exception as e:
        print(e) 
        return
    finally:
        print("The 'try except' is finished")   
main()