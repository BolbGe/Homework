dp = [0] * 3522

dp[1] = 1
for n in range(1, 3520):
    dp[n+1] = (2 * (n+1) - 1) * dp[n]

print(dp[2])