# Factorial using Recursion : 

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

n = 5
print(f"Factorial of {n} is {factorial(n)}")


# Output : 

# Factorial of 5 is 120