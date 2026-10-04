#  Find the Two Non-Repeating Elements (when others appear twice) :

def find_two_unique(arr):
    xor_all = 0
    for num in arr:
        xor_all ^= num

    # Rightmost set bit
    rightmost_set_bit = xor_all & -xor_all

    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num

    print("The two unique elements are:", num1, "and", num2)

arr = [2, 4, 7, 9, 2, 4]
find_two_unique(arr)


# Output :

# The two unique elements are: 7 and 9