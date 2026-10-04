# Find Maximum and Minimum in an Array : 

arr = [5, 3, 9, 1, 6]
max_val = arr[0]
min_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print(f"Maximum element is {max_val}")
print(f"Minimum element is {min_val}")


# Output : 

# Maximum element is 9
# Minimum element is 1