def fractional_knapsack(W, weights, profits):
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(len(weights))]
    ratio.sort(reverse=True)

    max_profit = 0
    for r, w, p in ratio:
        if W >= w:
            max_profit += p
            W -= w
        else:
            max_profit += r * W
            break

    return max_profit

weights = [10, 20, 30]
profits = [60, 100, 120]
W = 50
print(fractional_knapsack(W, weights, profits))  # Output: 240.0
