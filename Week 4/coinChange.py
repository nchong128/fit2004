import math
def coinChangeTopDown(coins, V):
    minCoins = math.inf

    for i in range(0,N):
        if coins[i] <= V:
            c = 1 + memo[V - coins[i]]

            if c < minCoins:
                minCoins = c

    memo[V] = minCoins

coinChangeTopDown([])


