# Clear the ith Bit of a Number :

def clear_bit(num, i):
    return num & ~(1 << i)

# Example
n = 10   # (1010 in binary)
i = 3    # clear 3rd bit
print("Original:", bin(n), "=", n)
print("After clearing bit", i, ":", bin(clear_bit(n, i)), "=", clear_bit(n, i))


# Output :

# Original: 0b1010 = 10
# After clearing bit 3 : 0b10 = 2