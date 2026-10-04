# GCD (Greatest Common Divisor) using Recursion : 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
a, b = 48, 18
print(f"GCD of {a} and {b} is {gcd(a, b)}")


# Output : 

# GCD of 48 and 18 is 6