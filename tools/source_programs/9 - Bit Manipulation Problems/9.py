# Find the Only Non-Repeating Element (when others appear twice) :

def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num  # XOR all elements
    return result

arr = [2, 3, 5, 4, 5, 3, 2]
print("The unique element is:", find_unique(arr))


# Output :

# The unique element is: 4