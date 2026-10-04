# Fibonacci series using Recursion : 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 10
print("Fibonacci series : ")
for i in range(n):
    print(fibonacci(i), end=" ")


# Output :

# Fibonacci series : 
# 0 1 1 2 3 5 8 13 21 34 