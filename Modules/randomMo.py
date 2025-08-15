import random as r

# # 1. random() → float in [0.0, 1.0)
# print(r.random()) # return float value like 0.7161138658435015
# # 2. randint(a, b) → random integer in [a, b]
# print(r.randint(1,10)) # return random int value between r.randint(a,b), a to b
# # 3. randrange(start, stop[, step]) → random integer
# print(r.randrange(0,10,2)) # Example: 8 (only even numbers)
# # 4. uniform(a, b) → random float in [a, b]
# print(r.uniform(1,5)) # Example: 3.142
# # 5. choice(seq) → pick 1 random element
# fruits = ["apple", "banana", "cherry"]
# print(r.choice(fruits)) # example = banana
# # 6. choices(seq, k=n) → pick n random elements (with replacement)
# print(r.choices(fruits,k=3))  # Example: ['apple', 'apple', 'cherry']
# # 7. sample(seq, k=n) → pick n random elements (without replacement)
# print(r.sample(fruits,2)) # Example: ['banana', 'apple']
# # 8. shuffle(seq) → shuffle list in place
# r.shuffle(fruits)
# print(fruits) # Example: ['cherry', 'apple', 'banana']
# # 9. seed(x) → set random seed for reproducibility
# r.seed(42)
# print(r.random()) # Same result every run if seed is same

print(r.randint(1,4))  # 1, 2, 3, or 4  ✅ (both ends inclusive)
print(r.randrange(1,4))  # 1, 2, or 3     ❌ (stop value exclusive)