# Search element in Array (Linear Search)

arr = [10, 20, 30, 40, 50]
target = 30
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

# Element 30 found at index 2