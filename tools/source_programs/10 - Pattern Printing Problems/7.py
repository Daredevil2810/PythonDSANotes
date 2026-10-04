# Diamond Pattern :

# Diamond Pattern
rows = int(input("Enter number of rows: "))

# Upper pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# Lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


# Output :

# Enter number of rows: 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *