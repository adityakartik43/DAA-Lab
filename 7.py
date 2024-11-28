def knapsack_01(W, weights, profits, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

weights = [1, 3, 4, 5]
profits = [1, 4, 5, 7]
W = 7
n = len(weights)
print(knapsack_01(W, weights, profits, n))  # Output: 9
