class Employee:
    language = "Python"
    salary = 100000000000

    def getInfo(self):
        print(f"The language is {self.language} .this salary is {self.salary}")

    @staticmethod # this allow to not use to self method
    def greed():
        print("Good Morning")
bhavin = Employee()

bhavin.getInfo()
# --
bhavin.greed()
# --- or ---
# Employee.getInfo(bhavin)