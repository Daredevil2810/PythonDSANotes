# Check if the ith Bit is Set :

# Given a number num and a position i, check if the ith bit in the binary representation of num is set (1) or not (0).

num = 13  # 1101
i = 2

mask = 1 << i

if (num & mask) != 0:
    print(f"Bit at position {i} is SET")
else:
    print(f"Bit at position {i} is NOT SET")


# Output :

# Bit at position 2 is SET