# Linear Search :

arr = [5, 10, 15, 20, 25]
target = 15
found_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f"Element {target} found at index {found_index}")
else:
    print(f"Element {target} not found")


# Output :

# Element 15 found at index 2