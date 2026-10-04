# Selection sort systematically : 

# Selection Sort repeatedly selects the minimum element from the unsorted part and places it at the beginning.

arr = [64, 25, 12, 22 , 11]
n = len(arr)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array : ", arr)


# Output :

# Sorted array :  [11, 12, 22, 25, 64]