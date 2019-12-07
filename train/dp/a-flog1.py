n = int(input())
h = list(map(int, input().split()))

INF = 10 ** 5 + 1

dp = [INF] * n

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, n):
    skip1 = dp[i - 1] + abs(h[i] - h[i - 1])
    skip2 = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(skip1, skip2)

print(dp[-1])
