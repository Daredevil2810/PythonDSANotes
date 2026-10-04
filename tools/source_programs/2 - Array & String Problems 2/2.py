# Reverse an Array :

arr = [1, 2, 3, 4, 5]
start = 0
end = len(arr)-1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array : ", arr)


# Output :

# Reversed array :  [5, 4, 3, 2, 1]