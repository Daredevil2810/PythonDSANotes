# Two sum problem (Find two numbers with target sum) :

arr = [2, 7, 11, 15, 1, 8]
target = 9
found = False

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Pair found: {arr[i]} + {arr[j]} = {target}\nTheir Index position are : {arr[i]} -> {i}, {arr[j]} -> {j}")
            found = True
            # break

    # if found:
    #     break

if not found:
    print("No pair found")


# Output : 

# Pair found: 2 + 7 = 9
# Their Index position are : 2 -> 0, 7 -> 1
# Pair found: 1 + 8 = 9
# Their Index position are : 1 -> 4, 8 -> 5
