# Counting sort systematically : 

# Counting Sort counts occurrences of each element and calculates their positions in the sorted array.

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:  # Count occurrences
        count[num] += 1

    for i in range(1, len(count)):  # Cumulative count
        count[i] += count[i - 1]

    for num in reversed(arr):  # Build output
        output[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]  # Copy back

arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Sorted array:", arr)


# Output :

# Sorted array: [1, 2, 2, 3, 3, 4, 8]