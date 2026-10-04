# Binary Search :

# Binary search repeatedly divides the search range in half until the element is found or the range is empty.

arr = [10, 20, 30, 40, 50]
target = 30
low, high = 0, len(arr) - 1
found_index = -1

while low <= high:
    mid = (low + high)//2
    if arr[mid] == target:
        found_index = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found_index != -1:
    print(f"Element {target} found at index {found_index}")
else:
    print(f"Element {target} not found")


# Output :

# Element 30 found at index 2