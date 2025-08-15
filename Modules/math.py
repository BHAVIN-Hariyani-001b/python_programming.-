import math as m

# print(dir(math))
# Use dir() → if you just want names of attributes/methods.
# print(math.__dict__)
# Use __dict__ → if you also need the values or want to filter by type.

# Mathematical constants ******
print("------------ Mathematical constants ------------")

print(m.pi) # Value of π (≈ 3.141592653589793)
print(m.e) # Euler’s number (≈ 2.718281828459045)
print(m.tau) # 2 × π (≈ 6.283185307179586)
print(m.pi * 2) # 2 × π (≈ 6.283185307179586)
print(m.inf) # positive infinity 
print(m.nan) # Not-a-Number (NaN)


# Basic math functions ********

print("------------ Basic math functions ------------")
print(m.sqrt(4)) # Square root of x
print(m.pow(2,4)) # x raised to power y
print(m.floor(2.74)) #  It is return to Smallest integer value like (2.74 => 2) and (2.24 => 2)
print(m.floor(2.24))
print(m.ceil(2.20))  # It is return to Largest integer value like (2.20 => 3) and (2.96 => 3)
print(m.ceil(2.96)) 
print(m.fabs(1)) # Absolute value (float)


# Factorial & combinations *********
print("------------ Factorial & combinations ------------")
print(m.factorial(5)) # Factorial of n
# C(n, k) = n! / (k! * (n - k)!)
print(m.comb(4,2)) # Combinations (n choose k) //   # Print total number of possible combinations 
print(m.perm(10,2)) # Permutations  # C(n, k) = n! / (n - k)!

# Trigonometric functions **********
print("------------ Trigonometric functions ------------")
print(m.sin(m.pi / 2)) # Sine of x (radians)
print(m.cos(0)) # Cosine
print(m.tan(m.pi / 4)) # Tangent
print(m.radians(180)) # Convert degrees → radians
print(m.degrees(m.pi)) # Convert radians → degrees  
 

# Logarithmic & exponential **********
print("------------ Logarithmic & exponential ------------")
print(m.log(m.e)) # Natural log (base e)
print(m.log10(100)) # Natural log (base e)
print(m.exp(2)) # e^x


# Checks ********
print("------------ Checks ------------")
print(m.isfinite(10)) # True if finite
print(m.isinf(m.inf)) # True if infinity
print(m.isnan(m.nan)) # True if NaN