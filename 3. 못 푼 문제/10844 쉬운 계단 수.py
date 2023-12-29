n = int(input())
dp = [[0 for _ in range(10)] for _ in range(101)]
# dp[a][b] = 길이가 a이며 맨 앞의 수가 b인 계단 수의 개수

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
