# Number Pyramid Pattern :

# Number Pyramid Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()


# Output : 

# Enter number of rows: 5
#     1
#    12
#   123
#  1234
# 12345