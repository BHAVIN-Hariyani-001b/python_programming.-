from abc import ABC, abstractmethod
# ******************************************
class Greet(ABC):
    @abstractmethod # it is use to not data access use in class out side
    def say_hello(self):
        # pass  # Abstract method
        print("Hello")
        print(self.__name)
        

class English(Greet):
    def say_hello(self):
        print("Hello!")

# c1 = Greet()
# c1.say_hello() # TypeError: Can't instantiate abstract class Greet without an implementation for abstract method 'say_hello'

# c2 = English()
# c2.say_hello()

c3 = Greet()
print(c3.__name)



# woithout use abc method ******************************************
# Base class acting as abstract class
class Vehicle:
    def start_engine(self):
        # Force subclasses to implement this method
        raise NotImplementedError("Subclass must implement start_engine method.")

    def stop_engine(self):
        print("Engine stopped.")

# Subclass implementing abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

# Another subclass implementing abstract method
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

# ------------------- Testing -------------------
car = Car()
car.start_engine()
car.stop_engine()

bike = Bike()
bike.start_engine()
bike.stop_engine()

# This will cause an error if not overridden
class Truck(Vehicle):
    pass

truck = Truck()
truck.start_engine()  # ❌ Raises NotImplementedError
  