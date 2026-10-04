# Swap Two Numbers without Temporary Variable (using XOR) :

# Swap two numbers using XOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before Swap: a = {a}, b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"After Swap: a = {a}, b = {b}")

# Output :

# Enter first number: 3  
# Enter second number: 5
# Before Swap: a = 3, b = 5
# After Swap: a = 5, b = 3