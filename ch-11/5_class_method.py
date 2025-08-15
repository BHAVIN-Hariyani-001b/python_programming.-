class Employee:
    a = 1

    @classmethod  # class method is to allow to calss proprty and method show in function 
    def show(cls):
        print(f"the calss value of a is {cls.a}")

    # proprty decoderator
    @property
    def name(self):
        return f"{self.fName} {self.lName}"
    
    #setter 
    @name.setter
    def name(self,value):
        self.fName = value.split(" ")[0]
        self.lName = value.split(" ")[1]

emp = Employee()
# emp.a = 12 # it is change to instance proprty in class but it is change only instace proprty it not change to class proprty

# emp.show() 
# Employee.a = 12  # it is change to class proprty in use to class 
# emp.show()

emp.name = "bhavin hariyani"
print(emp.fName)
print(emp.lName)
emp.show()




