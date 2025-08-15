"""
    ---Single Inheritance: A child class inherits from a single parent class.
    ---Multiple Inheritance: A child class inherits from more than one parent class.
    ---Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
    ---Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
    ---Hybrid Inheritance: A combination of two or more types of inheritance.



    --Single Inheritance (one parent → one child)
    --Multilevel Inheritance (grandparent → parent → child)
    --Multiple Inheritance (one child → many parents)
    --Hierarchical Inheritance (one parent → many children)
    --Hybrid Inheritance (mix all, Combination of multiple types) like  when I say Hybrid Inheritance is a “cocktail” of inheritance types, I mean it’s a mix of different inheritance patterns in one program.
"""

# 1
# Single Inheritance ***************************

# class Dog:
#     def __init__(self,name):
#         self.name = name
    
#     def display_name(self):
#         print(f"dog name is {self.name}")
        
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")

# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()

# 2
# Multilevel Inheritance ***************************
# class Dog:
#     def __init__(self,name):
#         self.name = name
    
#     def display_name(self):
#         print(f"dog name is {self.name}")
        
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")

# class GuideDog(Labrador):  
#     def guide(self):
#         print(f"{self.name}Guides the way!")

# guide_dog = GuideDog("max")
# guide_dog.display_name()
# guide_dog.sound()
# guide_dog.guide()


# 3 
# Multiple Inheritance ***************************

# class Dog:
#     def __init__(self,name):
#         self.name = name
    
#     def display_name(self):
#         print(f"dog name is {self.name}")

# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()

# 4
# Hierarchical Inheritance ***************************

# # Parent class
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# # Child class 1
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# # Child class 2
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")

# # Child class 3
# class Truck(Vehicle):
#     def load(self):
#         print("Truck is loading goods")

# # Create objects of each child class
# c = Car()
# b = Bike()
# t = Truck()

# # All children can use parent's method
# c.start()   # Vehicle started
# b.start()   # Vehicle started
# t.start()   # Vehicle started

# # Each child has its own methods
# c.drive()   # Car is driving
# b.ride()    # Bike is riding
# t.load()    # Truck is loading goods


# 5
# Hybrid Inheritance ***************************

# Parent Class
# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# # Child Class 1 (Single inheritance from Vehicle)
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# # Child Class 2 (Single inheritance from Vehicle)
# class Electric:
#     def battery(self):
#         print("Battery fully charged")

# # Child Class 3 (Multiple inheritance from Car and Electric)
# class Tesla(Car, Electric):
#     def autopilot(self):
#         print("Tesla is driving on autopilot")

# # Create object
# t = Tesla()

# # Methods from Vehicle (inherited through Car)
# t.start()

# # Method from Car
# t.drive()

# # Method from Electric
# t.battery()

# # Method from Tesla
# t.autopilot()
