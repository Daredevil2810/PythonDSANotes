# Set the ith Bit : 

def set_bit(num, i):
    return num | (1 << i)

# Example
n = 10   # (1010 in binary)
i = 1    # set 1st bit (counting from 0)
print("Original:", bin(n), "=", n)
print("After setting bit", i, ":", bin(set_bit(n, i)), "=", set_bit(n, i))


# Output :

# Original: 0b1010 = 10
# After setting bit 1 : 0b1010 = 10