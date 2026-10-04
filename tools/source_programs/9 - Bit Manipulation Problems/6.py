# Count Set Bits in a Number :

def count_set_bits(num):
    count = 0
    while num:
        count += num & 1   # check last bit
        num >>= 1          # right shift
    return count

# Example
n = 29   # (11101 in binary → 4 ones)
print("Number:", n, "Binary:", bin(n))
print("Set bits:", count_set_bits(n))


# Output :

# Number: 29 Binary: 0b11101
# Set bits: 4