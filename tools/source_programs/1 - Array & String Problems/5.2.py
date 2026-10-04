# Two sum problem (Find two numbers with target sum)
# using Dictionary (Hash Map) :

def two_sum_all_pairs(arr, target):
    seen = {}
    pairs = []

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            pairs.append((seen[complement], i))  # store indexes
        seen[num] = i   # save current number and index
    
    return pairs

# Example
arr = [2, 7, 11, 15, 1, 8, 2]
target = 9
result = two_sum_all_pairs(arr, target)

if result:
    for i, j in result:
        print(f"Pair found: {arr[i]} + {arr[j]} = {target} "
              f"\nTheir Index positions: {i}, {j}")
else:
    print("No pair found")


# Output : 

# Pair found: 2 + 7 = 9 
# Their Index positions: 0, 1
# Pair found: 1 + 8 = 9
# Their Index positions: 4, 5
# Pair found: 7 + 2 = 9
# Their Index positions: 1, 6
