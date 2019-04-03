import math

def bottomUp(V, coins):
    memo = [math.inf for i in range(V + 1)]

    # With a value of 0, can't use any coins
    memo[0] = 0

    # Iterate over table and fill based on recurrence relation
    for i in range(1, len(memo)):
        minCoins = math.inf

        # Iterate over all coins
        for j in range(len(coins)):
            if coins[j] <= i:
                c = 1 + memo[i - coins[j]]

                if c < minCoins:
                    minCoins = c

            memo[i] = minCoins

    return memo[-1]


def topDown(V, coins):
    memo = [math.inf for i in range(V + 1)]

    # With a value of 0, can't use any coins
    memo[0] = 0

    if memo[V] != math.inf:
        return memo[V]
    else:
        minCoins = math.inf
        for i in range(len(coins)):
            if coins[i] <= V:
                c = 1 + topDown(V - coins[i], coins)
                if c < minCoins:
                    minCoins = c
        memo[V] = minCoins
        return memo[V]

def main():
    V = int(input("Enter V: "))
    coins = [9,5,6,1]
    print("Coins are "+ str(coins) + "\n")

    print("Bottom up answer: " + str(bottomUp(V, coins)))

    print("Top down answer: " + str(topDown(V, coins)) + "\n")



if __name__ == '__main__':
    main()

'''
Problem 2
===============
a) The optimal solution to the highest profit from 10 houses is based on the optimal solutions
    with 9 houses, 8 houses, all the way down to 1 house.
b) Solving the highest profit from 10 houses will consider the profit from 1 house just like with solving the highest
    profit with 9 houses
c) If there are no houses => Profit = 0
    If there is just 1 house => Profit = House's value
        If there are 2 houses => Profit = Higher of the two
d) 
Two possible options with each house added
- The house is not added => Our optimal solution is the same as prev
- The house is added => Need to consider the optimal solution two spaces back AND with the prev number
Overall: dp[i] = max(dp[i-1], dp[i-2]+num[i-1])

e)
function doorToDoorSalesman(houses[1...n])
    memo[1...n] = 0
    
    if n == 1
        return houses[1]
    else if n == 2
        return max(houses[1], houses[2])
    
    for i = 1 to n
        if i == 1
            memo[i] = houses[i]
        else if i == 2
            memo[i] = max(houses[1], houses[2])
        else
            memo[i] = max(memo[i-1], memo[i-2] + houses[i-1])
                
    return memo[n]
    
    
    
    
    Note: task 8 related to assignment 2 => subwords instead of subarray

'''