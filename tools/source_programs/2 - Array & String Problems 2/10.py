# Check Palindrome String :

str_val = "Madam"
lower_str = str_val.lower()
is_palindrome = True

for i in range(len(lower_str)):
    if lower_str[i] != lower_str[-1 -i]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{str_val} is a palindrome")
else:
    print(f"{str_val} is not a palindrome")


# Output :

# Madam is a palindrome