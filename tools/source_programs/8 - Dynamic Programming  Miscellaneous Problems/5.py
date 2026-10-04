# Maximum Subarray Sum Problem (Kadane’s Algorithm) :

def max_subarray(arr):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray(arr))


# Output :

# Maximum Subarray Sum: 6