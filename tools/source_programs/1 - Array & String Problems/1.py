# Find the Largest Element in an Array : 

arr = [10,20,5,14,35]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
        
print("Largest element is", max_val)


# Output : 

# Largest element is 35