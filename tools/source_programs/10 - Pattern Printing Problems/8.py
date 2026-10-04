# Hollow Diamond Pattern :

# Hollow Diamond Pattern
rows = int(input("Enter number of rows: "))

# Upper hollow pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower hollow inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Output : 

# Enter number of rows: 5
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *