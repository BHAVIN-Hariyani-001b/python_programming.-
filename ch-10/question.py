# 1

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
    
    def getInfo(self):
        print(f" name is : {self.name} \n company name is : {self.company} \n salary is : {self.salary} \n picode is : {self.pincode}")
        

# bhavin = Programmer("bhavin",100000000000000,365601)
# bhavin.getInfo()

# anand = Programmer("anand",100000000000000,365601)
# anand.getInfo()


# 2

class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num * self.num
    
    def cube(self):
        return self.num * self.num * self.num
    
    def squareRoot(self):
        return self.num ** 0.5
    
# a = Calculator(4)
# print(f"square is : {a.square()}")  
# print(f"cube is : {a.cube()}")
# print(f"square root is :{a.squareRoot()}")


# 3
class Demo:
    a = 4

# o = Demo()
# print(o.a) # print to the class atribute print because instace attribute is not present  
# o.a = 0 # instace attribute is set 
# print(o.a) # print attribute is instace
# print(Demo.a) # print to calss attribute
# Demo.a = 0 # chaneg to class attribute
# print(Demo.a) # print to calss attribute // it is set to class and instance attribute change automatic
# print(o.a) # print to calss attribute


# 4

class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num * self.num
    
    def cube(self):
        return self.num * self.num * self.num
    
    def squareRoot(self):
        return self.num ** 0.5
    
    @staticmethod
    def hello():
        print("Hello There")

# a = Calculator(4)
# a.hello()
# print(f"square is : {a.square()}")  
# print(f"cube is : {a.cube()}")
# print(f"square root is :{a.squareRoot()}")


# 5
from random import randint as random

class Train:
    def __init__(self,trainNum):
        self.trainNum = trainNum

    def book(self,fro,to):
        print(f"ticket is book in train number {self.trainNum} from {fro} to {to}")

    def getStatus(self,trainNum):
        print(f"train no {trainNum} runnig successfuly")

    def getFareInformation(self,fro,to):
        print(f"ticket fare in train number {self.trainNum} from {fro} to {to} is {random(2222,5555)}")
    

# t = Train(123243)
# t.book("Amreli","Ahemadabad")
# t.getStatus(123243)
# t.getFareInformation("Amreli","Ahemadabad")


# 6

from random import randint as random


# use can use to self than change to remove self and write your_name and it same work to like self BUT THIS IS NOT GOOD WHEY TO PRECTICE TO PROBLEM AND READEBILITY IS VERY WRONG TO YOUR PROGRAM
class Train:
    def __init__(jay,trainNum):
        jay.trainNum = trainNum

    def book(jay,fro,to):
        print(f"ticket is book in train number {jay.trainNum} from {fro} to {to}")

    def getStatus(trainNum):
        print(f"train no {trainNum} runnig successfuly")

    def getFareInformation(jay,fro,to):
        print(f"ticket fare in train number {jay.trainNum} from {fro} to {to} is {random(2222,5555)}")
    


