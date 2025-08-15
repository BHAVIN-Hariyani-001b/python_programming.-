# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression."

# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
 
# Output: List is too long (5 elements, expected <= 3) 

print((n := 6) > 4) # () breket is work to assing first and comparesion
print(n)