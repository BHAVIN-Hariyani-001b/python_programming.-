#1 write a program and store to fruits name

fruits = []
for i in range(5):
    fruits.append(input("Enter your fruits : "))
print(end="\n")
print(fruits)

# or 

fruits = [input("enter fruits name :") for i in range(5)]
print(fruits)

# 2 write a program to enter student mark's ***

student = []
for i in range(6):
    student.append(int(input("Enter Student Mark :")))
student.sort()
print(student)

# OR

student = [int(input("Enter student mark : ")) for i in range(6)]
student.sort()
print(student)


# 3 tuple creata and check to update and try to update

a = (43,64,65,74,234,"bhavin")
a[2] = "abc"
print(a)

# 4  sum of all index value
l = [32,43,54,65]
print(sum(l)) # it is sum of all number in use to sum bild-in function

# 5 count to 0 in tuple

a = (7,0,8,0,0,9)
print(a.count(0))