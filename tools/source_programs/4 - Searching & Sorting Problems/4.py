# Bubble sort systematically :

# Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.(It start with pushing the largest elment to the end of arr)

arr = [64, 34, 25, 12, 22]
n = len(arr)

for i in range(n - 1):
    for j in range(n -i -1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array : ", arr)


# Output :

# Sorted array :  [12, 22, 25, 34, 64]