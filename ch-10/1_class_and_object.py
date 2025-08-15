class Employee: # this is class atribute
    # property
    laguage = "python"
    salary = 100000000000

bhavin = Employee()
bhavin.name = "abc"
print(bhavin.name)
print(bhavin.laguage)
print(bhavin.salary)

anand = Employee()
anand.name = "xyz"
anand.laguage = "CPP"
print(anand.name)
print(anand.laguage)
print(anand.salary)

print(Employee.__dict__) ## it is use to show all proprty in use to in this class
    


