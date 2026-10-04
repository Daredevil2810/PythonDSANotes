# LCM (Least Common Multiple) using GCD :

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = 48, 18
print(f"LCM of {a} and {b} is {lcm(a, b)}")


# Output : 

# LCM of 48 and 18 is 144