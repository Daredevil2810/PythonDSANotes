# Check Prime number : 

n = 2
is_prime = True

if n < 2:
    is_prime = False

for i in range(2, int(n**0.5) + 1):    # (n**0.5) means sqrt(n)
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")


# Output : 

# 2 is prime