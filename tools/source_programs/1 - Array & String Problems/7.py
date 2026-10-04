# Find second largest element in array : 

arr = [1, 10, 4, 11, 23, 5]
first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest element is ", second)


# Output :

# Second largest element is  11