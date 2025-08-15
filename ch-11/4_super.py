# super() method is used to access the methods of a super class in the derived class

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# mutileve ingaritace ********

# class Employee:
#     a = 1
#     def __init__(self):
#         print("Constructor of Employee")
# class Programmer(Employee):
#     b = 2
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Programmer")
# class Manager(Programmer):
#     c = 3
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")

# e = Employee()
# print(e.a)

# p = Programmer()
# print(p.a)
# print(p.b)

# m = Manager()
# print(m.a)
# print(m.b)
# print(m.c)


# # muti level inharitance
# # use to like this in muti level but most off use to try super() key word syntax

class Employee:
    def __init__(self,ename):
        self.ename = ename
    def empName(self):
        print(f"Employee name is {self.ename}")

class Programmer(Employee):
    def __init__(self,ename,pname):
        super().__init__(ename)
        # use to like this in muti level but most off use to try super() key word syntax
        # Employee.__init__(self,ename,pname)
        self.pname = pname

    def proName(self):
        print(f"Programer name {self.pname}")

class Manager(Programmer):
    def __init__(self,ename,pname,mname):
        super().__init__(ename,pname)
        # use to like this in muti level but most off use to try super() key word syntax
        # Programmer.__init__(self,ename,pname)
        self.mname = mname

    def manName(self):
        print(f"Manager name {self.mname}")

emp = Employee("bhavin")
emp.empName()

pro = Programmer("bhavin","anand")
pro.empName()
pro.proName()

man = Manager("bhavin","anand","hariyani")
man.empName()
man.proName()
man.manName()


    