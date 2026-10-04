# Reverse a number using Recursion :

def reverse_num(n, rev = 0):
    if n == 0:
        return rev
    else:
        return reverse_num(n // 10, rev * 10 + n % 10)

n = 12345
print(f"Reverse of {n} is {reverse_num(n)}")


# Output :

# Reverse of 12345 is 54321