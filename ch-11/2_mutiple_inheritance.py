class Employee:
    company = "ITC"

    name = "Bhavin"
    def show(self):
        print(f"The name of the employee {self.name} and company is {self.company}")

class Coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all the language's here is your language's is {self.language}")

# mutiple inharitance
class Programmer(Employee,Coder):
    company = "ITC Infotach"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")


c1 = Employee()
c2 = Programmer()

c2.show()
c2.printLanguages()
c2.showLanguage()


