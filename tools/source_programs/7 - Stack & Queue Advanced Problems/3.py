# Next Greater Element Problem :

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

arr = [4, 5, 2, 25]
nge = next_greater_element(arr)
print("Next Greater Elements:", nge)


# Output : 

# Next Greater Elements: [5, 25, 25, -1]