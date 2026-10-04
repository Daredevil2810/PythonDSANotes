# Reverse an Array :

arr = [10,20,30,40,50]

start = 0
end = len(arr) - 1

while start < end:

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start += 1
    end -= 1

print("Reversed array : ", arr)


# Output : 

# Reversed array :  [50, 40, 30, 20, 10]