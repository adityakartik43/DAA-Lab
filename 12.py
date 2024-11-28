def lcs(S1, S2):
    m, n = len(S1), len(S2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

S1 = "ABCBDAB"
S2 = "BDCAB"
print(lcs(S1, S2))  # Output: 4
