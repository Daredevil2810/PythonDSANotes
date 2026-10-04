# Binary Search (Recursive Method) :

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [10, 20, 30, 40, 50]
target = 30
index = binary_search(arr, target, 0, len(arr)-1)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")


# Output :

# Element 30 found at index 2