# Check if a Number is Even or Odd using Bitwise Problem :

# Bit manipulation problems are very common in coding interviews. They test your understanding of how integers are stored in binary and how bitwise operators (&, |, ^, ~, <<, >>) work.

num = 7

if (num & 1) == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# Output :

# 7 is Odd