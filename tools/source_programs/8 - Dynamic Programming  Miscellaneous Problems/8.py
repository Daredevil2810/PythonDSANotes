# Maximum Product Subarray Problem :

def max_product_subarray(arr):
    max_ending = arr[0]
    min_ending = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_ending, min_ending = min_ending, max_ending

        max_ending = max(arr[i], arr[i] * max_ending)
        min_ending = min(arr[i], arr[i] * min_ending)

        max_so_far = max(max_so_far, max_ending)
    return max_so_far

arr = [2, 3, -2, 4]
print("Maximum Product Subarray:", max_product_subarray(arr))


# Output :

# Maximum Product Subarray: 6