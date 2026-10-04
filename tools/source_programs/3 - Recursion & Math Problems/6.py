# Sum of digits using Recursion : 

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
    
n = 12345
print(f"Sum of digits of {n} is {sum_of_digits(n)}")


# Output : 

# Sum of digits of 12345 is 15