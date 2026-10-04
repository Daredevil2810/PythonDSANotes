# Minimum Coin Change Problem :

def min_coins(coins, V):
    dp = [float('inf')] * (V+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, V+1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[V] == float('inf') else dp[V]

coins = [1, 2, 5]
V = 11
print("Minimum Coins Needed:", min_coins(coins, V))


# Output :

# Minimum Coins Needed: 3