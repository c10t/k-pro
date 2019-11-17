from collections import defaultdict

n, t = map(int, input().split())
menu = []

for _ in range(n):
    a, b = map(int, input().split())
    menu.append((a, b))

menu = sorted(menu)

dp = defaultdict(int)
dp[0] = 0

score = 0

for a, b in menu:
    for time, utility in list(dp.items()):
        if time + a >= t:
            score = max(score, utility + b)
        else:
            dp[time + a] = max(dp[time + a], utility + b)

print(max(score, max(dp.values())))
