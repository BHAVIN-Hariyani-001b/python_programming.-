class Employee:
    language = "Python"
    salary = 100000000000

    # dunder metnod it like start with __ 
    # this is constructor it is atomatic call to create object
    def __init__(self,name,salary,language):
        print("I am creating an object") #Constructor
        self.name = name  # Assign value to object variable
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language} .this salary is {self.salary}")

    @staticmethod # this allow to not use to self method
    def greed():
        print("Good Morning")

# Creating object and passing value
bhavin = Employee("jay",13000000,"Javascript")
print(bhavin.name,bhavin.salary,bhavin.language)
# overrides 
bhavin.name = "roy" # Dynamically adds the `name` attribute to the bhavin object
print(bhavin.name,bhavin.salary,bhavin.language)

print(Employee.language) # class name use and access value and metho in calss
# ✅ OK — Access class variable using class name 👆
# Employee.getInfo() # ❌ not allow to use and pass to value 
# ❌ ERROR — getInfo needs an instance (uses `self`) 👆
Employee.getInfo(bhavin)
Employee.greed() # ✅ OK — because it's a static method