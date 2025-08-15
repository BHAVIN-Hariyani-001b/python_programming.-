"""
Types of Encapsulation:
    -- Public Members: Accessible from anywhere.
    -- Protected Members: Accessible within the class and its subclasses.
    -- Private Members: Accessible only within the class.
"""

# without use @pproperty and setter and getter create ******************************************
class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)
dog.__age
# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())


# getter and setter use to @pproperty decorator ******************************************

class Employee:
    # Constructor method to initialize object attributes
    def __init__(self, name, age, salary, city):
        self.name = name              # Public attribute
        self.__age = age              # Private attribute (double underscore)
        self.__salary = salary        # Private attribute
        self._city = city             # Protected attribute (single underscore)

    # Protected method to display employee details
    def _Show(self):
        # Accessing both public and private attributes inside the class
        print(f"name is {self.name}")
        print(f"age is {self.__age}")
        print(f"salary is {self.__salary}")
        print(f"city is {self._city}")

    # Getter method for age (read-only access)
    @property
    def get_age(self):  
        return self.__age  # Return private __age value
    
    # Setter method for age (controlled write access)
    @get_age.setter
    def get_age(self, value):
        # Validate that the age is greater than 18
        if value > 18:
            self.__age = value
        else:
            print("Age must be greater than 18!")  # Validation error message


# ------------------- Testing the Class -------------------

# Creating Employee object with initial values
emp = Employee("Alice", 25, 50000, "amr")

# Displaying all details using the protected method
emp._Show()

# Getting private __age using getter property
print(emp.get_age)  

# Setting new valid age using setter property
emp.get_age = 30
print(emp.get_age)

# Trying to set invalid age (less than or equal to 18)
emp.get_age = 15  # Will print validation error
print(emp.get_age)
