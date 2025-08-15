class Book:
    def __init__(self,name,page):
        self.page = page
        self.name = name

    # dunder methods is start to __
    
    def __add__(self,value):
        return self.page + value.page
    
    def __str__(self):
        return f"name is {self.name}"
    
    def __repr__(self):
        return f"Book(name='{self.name}', pages={self.page})"
    
    def __len__(self):
        return self.page

    def __sub__(self,value):
        return self.page - value.page
    
    def __mul__(self,value):
        return self.page * value.page
    
    def __eq__(self, value):
        return self.page == value.page
    
    def __lt__(self, value):
        return self.page < value.page


str1 = Book("bhavin",10)
str2 = Book("hariyani",5)
# print(str1)
# print(repr(str1))  
# print(len(str1))
## print(str1 + str2)
##     it is same to 👇👆
## print(str1.__add__(str2))
# print(str1 - str2)
# print(str1 * str2)
# print(str1 == str2)
# print(str1 < str2)



        

