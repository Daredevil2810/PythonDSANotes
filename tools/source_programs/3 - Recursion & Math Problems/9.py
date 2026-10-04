# Count Number of Digits using Recursion : 

def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
    
n = 12345
print(f"Number of digits in {n} is {count_digits(n)}")


# Output : 

# Number of digits in 12345 is 5