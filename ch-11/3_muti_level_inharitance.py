# mutileve ingaritace ********

class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

m = Manager()
print(m.a)
print(m.b)
print(m.c)


