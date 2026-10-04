# Reverse a string : 

str_val = "HelloWorld"
reversed_str = ""

for i in range(len(str_val)-1, -1, -1):
    reversed_str += str_val[i]

print("Reversed string: ", reversed_str)


# Output : 

# Reversed string:  dlroWolleH