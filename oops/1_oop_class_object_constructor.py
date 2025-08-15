"""
ALL TOPIC --- OOP
https://www.geeksforgeeks.org/python/python-oops-concepts/

 --- total topic --- 
 -- in this file exe..
1 . what is class 
2 . what is instance
3 . what is method 
4 . what is proprty
5 . how to create object
6 . how to access object function and proprty
7 . self keyword
8 . deffrent between class variable and instace variable
9 . what is constructor and diffrent between defualt and peramiter constructor 
10 . how to change instance variable value and class variable value 
"""

# NORMAL CLASS ******
# and create proprty and method in class

# class Car:
#     a = "BMW"
#     def Start():
#         print("Start car")

#     def Stop():
#         print("Stope car")

# #  you can create normal calss and not use self keyword and class not call to create object 👇
# bmw = Car # like // and it start and show method is static method and it is not call to class and it only not class call to in static method use 
# bmw.Start() 
# bmw.Stop()
# bmw.a = "Totota" #// it change to class proprty change useing bmw object
# print(bmw.a)


# USE TO SELF KEYWORD AND MUTIPLE OBJECT CREATE**

# class Person:
#     name = "bhavin"
#     age = 21

#     def info(self): #self is use to specific to call the object  like create persone object and call
#         print(f"name is {self.name} and age is {self.age}")

# p1 = Person()
# print(p1.name)
# print(p1.age)
# p1.info()

# p2 = Person()
# p2.age = 12
# p2.name = "anand" # you can change to instance value
# p2.info()




# USE TO CONSTRUCTOR ******
# DEFUALT CONSTRUCTOR
class a:
    def __init__(self):
        print("hi")
# a = a()
# PERAMITER CONSTRUCTOR 
class Persone:
    # dundor method is start to with __ and and with __ like __init__()
    # __init__ method is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


# a = Persone("Bhavin","founder")
# a.info()
# a = Persone("anand","ceo")
# a.info()


class Dog:
    specish = "canine"

    def __init__(self,name,age):
        self.name = name
        self.age = age


# create object
dog1 = Dog("abc",4)
dog2 = Dog("xyz",5)

# Access class and instance variables
print(dog1.specish) # class variables
print(dog1.name) # instance variables
print(dog1.age) # instance variables


# Modify instance variables
dog1.name = "mqr"
print(dog1.name) #  # (Updated instance variable)

# Modify class variable

Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)


        
