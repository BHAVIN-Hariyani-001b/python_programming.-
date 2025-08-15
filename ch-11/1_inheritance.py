class Employee:
    company = "ITC"
    name = "BHavin"
    def show(self):
        print(f"The name of the employee {self.name} and salary is {self.company}")

class Programmer(Employee):
    def showLanguage(slef,language):
        print(f"company name is {slef.company}")
        print(f"Programin language is {language}")

     
# c1 = Employee("bhavin",100000000000000)
# c1.show()
# c2 = Programmer("bhavin",1000000000000000)
# c2.show()
# c2.showLanguage("Python")


class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"first name is {self.fname} and last name is {self.lname}")

class Student(Person):
    # it is use to all and easy *****
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    # it is use to only in single inharitace *******
    # def __init__(self,fname,lname):
    #     Person.__init__(self,fname,lname)

# abc = Student("bhavin","hariyani")
# abc.printname()


    



        


