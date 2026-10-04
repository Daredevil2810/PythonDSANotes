# Power of a number using Recursion :

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
    
a, b = 2, 5
print(f"{a}^{b} = {power(a, b)}")


# Output : 

# 2^5 = 32