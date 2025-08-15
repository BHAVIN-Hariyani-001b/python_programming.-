"""
Two type of Polymorphism
 -- Compile-Time Polymorphism
 -- Run-Time Polymorphism
"""

# 1 exe ...
# Parent Class
# class Dog:
#     def sound(self):
#         print("dog sound")  # Default implementation

# # Run-Time Polymorphism: Method Overriding
# class Labrador(Dog):
#     def sound(self):
#         print("Labrador woofs")  # Overriding parent method

# class Beagle(Dog):
#     def sound(self):
#         print("Beagle Barks")  # Overriding parent method

# # Compile-Time Polymorphism: Method Overloading Mimic
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c  # Supports multiple ways to call add()

# # Run-Time Polymorphism
# dogs = [Dog(), Labrador(), Beagle()]
# for dog in dogs:
#     dog.sound()  # Calls the appropriate method based on the object type


# # Compile-Time Polymorphism (Mimicked using default arguments)
# calc = Calculator()
# print(calc.add(5, 10))  # Two arguments
# print(calc.add(5, 10, 15))  # Three arguments

# # 2 exe...

# class Game:
#     def play(self):
#         print("🎮 Playing the game...")

# class Music:
#     def play(self):
#         print("🎵 Playing music...")

# class Video:
#     def play(self):
#         print("🎬 Playing video...")

# class AudioBook:
#     def play(self):
#         print("🎧 Playing audiobook...")

# # Function that works with ANY object having a play() method
# def start_media(media_item):
#     media_item.play()

# # Create objects
# g = Game()
# m = Music()
# v = Video()
# a = AudioBook()

# # Using polymorphism: same function, different behavior
# start_media(g)  # 🎮 Playing the game...
# start_media(m)  # 🎵 Playing music...
# start_media(v)  # 🎬 Playing video...
# start_media(a)  # 🎧 Playing audiobook...


# Operator Overloading ***************************
# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because '+' operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

# Python program to show use of
# + operator for different purposes.

# print(1 + 2)

# # concatenate two strings
# print("Geeks"+"For") 

# # Product two numbers
# print(3 * 4)

# # Repeat the String
# print("Geeks"*4)




# getter and setter *********************
class Myclass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"value is {self.value}")

    @property
    def tan_value(self):
        return 10 * self.value
    
    @tan_value.setter
    def tan_value(self,new_value):
        self.value = new_value / 10

obj = Myclass(1)
print(obj.tan_value)
obj.show()
obj.tan_value = 100
obj.show()
print(obj.tan_value)
obj.show()