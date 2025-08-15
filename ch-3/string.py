#string *************
#string is immutable
#Type of 3 

# 1st type *      
#   
# a = "bhavin"
# print(a)
# print(a[3]) # print to like array use to string and start index is 0 is first and -1 is a last of string
# print(a[-1])

# 2nd type *

# b = """hi bhavin 
# it is good"""
# print(b)

# 3nd type *

# c = '''hi bhavin is all 
# good'''
# print(c)


# for i in c:
#     print(i,end="_")
# print(end="\n")

# if "hi" in c:
#     print("yes")
# else:
#     print("no")

# concatination *************


# a = 'hariyani'
# b = "bhavin"
# print(a + b)
# print(a + " " + b)


# c = "2"
# d = "5"
# print(c+d)


# slicing ************
 
# b = "bhavin hariyani"
# print(b[:4])
# print(b[0:])
# print(b[1:6])
# print(b[1:-1])
# print(b[1:]) # remove first chareacter
# print(b[:-1]) #remove last chareacter

# print(b[-8:-1]) # simple understand 
# length of string  15 - 8 = 7
# length of string 15 - 1 = 14
#It is same to nagative or positive
# print(b[7:14])

 
# first value pass to starting index --- *_*
# second value pass to ending index
# slicing is pass to thred value it is work to step and how many stpe jump in string and it also use to array(list)

# print(b[::2]) # it is use to all value but 
# print(b[0::1])
# print(b[0:6:1]) 
# print(b[0:6:1]) #It therd value pass it automatic 1(one)  
# print(b[::-2]) # reverse skip 2 step

# copy string ************

# a = b[:] # Shallow copy 
# print(a)

# string reverse ************
# print(b[::-1]) 

# function **************
# string is not change you can function use and function return new value 



# a = "hello"
# a = a.upper()
# print(a)
# a = a.lower()
# print(a)

# s = "  hello  "
# print(s.strip())   # "hello"
# print(s.lstrip())  # "hello  "
# print(s.rstrip())  # "  hello"

# s = "I love Java Java"
# print(s.replace("Java", "Python"))  # "I love Python" 
# s = "I love Java"
# print(s.replace("Java", "Python"))  # "I love Python" 
#  it is all value replace to pass  

# b = "bhavin hariyani"
# print(b.split(" ")) #it is pass to value like {,  | '' | - } etc like string availabe to pass 

# s = "a,b,c"
# parts = s.split(",")  # ['a', 'b', 'c'] ,, split is convert to list{array}
# print(parts)
# print(",".join(parts))  # "a,b,c" ,, join is work join array item and pass value and like , . - ? _ " "  | etc....

# print(len(a)) # it is use to lenght return 
# print(a.endswith("llo"))# it is check to string is end with "pass to string " and check and return true and false 
# print(a.endswith("ad"))

# print(a.startswith("h")) # it is same like endwith() function
# print(a.startswith("a"))

# print(a.capitalize()) # it is use to frist character capitalize 
# print(a.title())    # it is same like capitalize() function
# s = "hello world"
# Finds the position of a substring.
# print(s.find("world"))  # 6
# print(s.find("python")) # not find and return -1 

# index() raises error if not found
# print(s.index("hello"))  # 0 it is return index
# print(s.index("python"))  # not find index in string and return ERROR

# print("123".isdigit())    # True
# print("abc".isalpha())   # True
# print("abc123".isalnum())  # True

# s = "banana"
# # Counts how many times a substring appears.
# print(s.count("a"))  # 3 (it is count to pass value is repet to in string)

name = "Alice"
age = 21

# format()
print("My name is {} and I am {} years old.".format(name, age))

# f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")



#  f string  ----> formate string

# age = 18
# name = "Bhavin"
# print(f"my name {name} and age is {age}")


# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# tex = f"The price is {20 * 59} dollars"
# print(tex)

# To fix this problem, use the escape character \":



# Escape Character **********
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# txt = "We are the so-called \"Vikings\" from the north." # it is minig remove to interpertr and use to {\} <--- this use
# print(txt)
# txt = 'It\'s alright.' #Single Quote
# print(txt)
# txt = "This will insert one \\ (backslash)." # Backslash
# print(txt) 
# txt = "Hello\nWorld!" #New Line
# print(txt) 
# txt = "Hello\rWorld!" # Carriage Return
# print(txt) 
# txt = "hello\tworld!" # tab
# print(txt) 
# txt = "Hello \bWorld!" #	Backspace
# print(txt)
# txt = "\110\145\154\154\157" #	Octal value
# print(txt) 
# txt = "\x48\x65\x6c\x6c\x6f" # Hex value
# print(txt) 