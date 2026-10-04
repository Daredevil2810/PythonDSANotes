# Count occurances of element in Array :

arr = [10, 20, 30, 20, 10, 20]
target = 20
count = 0

for i in arr:
    if i == target:
        count += 1
    
print(f"Element {target} occurs {count} times")


# Output : 

# Element 20 occurs 3 times