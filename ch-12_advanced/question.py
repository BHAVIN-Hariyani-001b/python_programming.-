# 1 

# try:
#     with (
#     open("ch-12_advanced/file1.txt") as f1,
#     open("ch-12_advanced/file2.txt") as f2,
#     open("ch-12_advanced/filename.txt") as f3
#     ):
#         print(f1.read(),f2.read(),f3.read())
# except FileNotFoundError as e:
#     print(f"Error : {e}")
    
# 2

# l = [1,2,3,4,5,6,7,8,9,10]
# for idx,value in enumerate(l,1): # enumerate function pass two value first is list,tuple.. and second is start 1,2, ext...
#     if idx in [3,5,7]:
#         print(f"index is '{idx}' and value is '{value}'")

# 3

# n = int(input("Enter table number : "))
# table = [n*i for i in range(1,11)]
# print(table)

# table = [f"{n} x {i} = {n*i}" for i in range(1,11)]
# print(table)
# for i in table:
#     print(i)

# 4

# try:
#     a = int(input("Enter your number : "))
#     b = int(input("Enter your number : "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"Error : Infinite")

# 5 
# with open("ch-12_advanced/table.txt"):

n = int(input("Enter table number : "))
table = [n*i for i in range(1,11)]
print(table)
with open("ch-12_advanced/table.txt","a") as f:
    f.write(f"table number : {n} : {table}\n")

        