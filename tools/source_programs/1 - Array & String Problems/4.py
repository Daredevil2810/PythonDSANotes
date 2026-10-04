# Count Occurrences of an Element in an Array :

arr = [1, 2, 3, 4, 2, 5]

target = 2
count = 0

for num in arr:
    if num == target:
        count += 1

print(f"Element {target} occurs {count} times")


# Output : 

# Element 2 occurs 2 times