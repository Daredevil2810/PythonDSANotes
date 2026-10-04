# Fibonacci Series Using Dynamic Programming :

def fibonacci_dp(n):
    if n == 0: return []
    if n == 1: return [0]

    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp

n = 10
fib = fibonacci_dp(n)
print("Fibonacci Series:", fib)


# Output :

# Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]