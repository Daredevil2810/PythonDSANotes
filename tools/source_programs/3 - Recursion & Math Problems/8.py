# Check Palindrome number using Recursion : 

def reverse_num(n, rev = 0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_num(n)

n = 12321
print(f"{n} is a palindrome" if is_palindrome(n) else f"{n} is not a palindrome")


# Output :

# 12321 is a palindrome