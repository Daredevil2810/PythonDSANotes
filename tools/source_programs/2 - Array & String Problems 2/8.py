# Reverse a String :

str_val = "Hello World"
# reversed_str = str_val[::-1]

reversed_str = ""
for ch in str_val:
    reversed_str = ch + reversed_str

print("Reversed string : ", reversed_str)


# Output : 

# Reversed string :  dlroW olleH