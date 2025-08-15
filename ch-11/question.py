# 1
class twoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is {self.i + self.j}")

class ThreeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The Vector is {self.i + self.j + self.k}")
    
# a = twoDVector(1,2)
# b = ThreeDVector(1,2,3)

# a.show()
# b.show()


# 2
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

# d = Dog()
# d.bark()

# 3
class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    # OR
    # def salaryAfterIncrement(self):
    #     return self.salary + self.salary * self.increment
        
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary / self.salary) - 1) * 100
        


# abc = Employee() 
# # print(abc.salaryAfterIncrement)
# abc.salaryAfterIncrement = 280
# print(abc.increment)

# 4

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"
    

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1 * c2)

# 5

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z)

    def __mul__(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
    
# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)


# 6



class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y,self.z + other.z)

    def __mul__(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)
# v3 = Vector(7,8,9)

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)

        
# 7
class Vector:
    def __init__(self,l):
        self.l = l
    
    def __len__(self):
        return 3
    
v1 = Vector([1,2,3])
print(len(v1))
