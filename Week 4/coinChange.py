import math
def coinChangeTopDown(coins, V):
    memo = [math.inf] * V
    memo[0] = 0

    for v in range(0,V):
        minCoins = math.inf

        for i in range(0, len(coins)):
            if coins[i] <= V:
                c = 1 + memo[V - coins[i]]

                if c < minCoins:
                    minCoins = c
        memo[V] = minCoins

coinChangeTopDown([9,5,6,1], 12)


