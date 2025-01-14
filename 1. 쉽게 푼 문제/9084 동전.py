t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m + 1)]
    # dp[i] = i원을 만들 수 있는 경우의 수
    dp[0] = 1

    for coin in a:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]
            # i를 만들 수 있는 경우의 수에,
            # i - coin을 만든 뒤 coin을 추가하는 경우의 수를 더함

    print(dp[m])
