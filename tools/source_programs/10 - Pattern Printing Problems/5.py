# Pyramid Pattern :

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Output :

# Enter number of rows: 5
#     *
#    ***
#   *****
#  *******
# *********