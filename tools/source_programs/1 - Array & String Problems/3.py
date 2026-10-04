# Check if a string is a palindrome : 

# str_val = "Hello"
str_val = "lolol"
is_palindrome = True

start = 0
end = len(str_val) -1

while start < end:
    if str_val[start] != str_val[end]:
        is_palindrome = False
        break

    start += 1
    end -= 1

if is_palindrome:
    print(f"{str_val} is a palindrome")
else:
    print(f"{str_val} is not a palindrome")


# Output : 

# lolol is a palindrome