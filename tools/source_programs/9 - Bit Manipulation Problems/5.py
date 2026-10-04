# Toggle the ith Bit of a Number :

def toggle_bit(num, i):
    return num ^ (1 << i)

# Example
n = 10   # (1010 in binary)
i = 2    # toggle 2nd bit
print("Original:", bin(n), "=", n)
print("After toggling bit", i, ":", bin(toggle_bit(n, i)), "=", toggle_bit(n, i))


# Output :

# Original: 0b1010 = 10
# After toggling bit 2 : 0b1110 = 14