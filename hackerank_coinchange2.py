__author__ = 'Rushil'

t, n = map(int, input().split())
nums = list(map(int, input().split()))
dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
for i in range(1, n+1):
    for j in range(1, t+1):
        dp[i][j] = dp[i-1][j]
        if j >= nums[i-1]:
            dp[i][j] += dp[i][j-nums[i-1]]
print(dp[-1][-1])
