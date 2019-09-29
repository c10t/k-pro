# Python 3 (3.4.3) => TLE
# PyPy3 (2.4.0) => AC

n, m = map(int, input().split())
prices = []
keymap = []
for _ in range(m):
    a, b = map(int, input().split())
    prices.append(a)
    c = list(map(int, input().split()))
    state = 0
    for ck in c:
        state |= 1 << ck - 1
        # print(format(state, "b"))
    keymap.append(state)

# print(keymap)

dp = [float("inf")] * (1 << n)  # 2 ** n
dp[0] = 0

for price, keyto in zip(prices, keymap):
    # print("--- step start ---")
    # print(dp)
    dp_new = dp[:]
    for s, d in enumerate(dp):
        # print("=== DP ===")
        # print("s:", format(s, "b"))
        # print("c:", format(keyto, "b"))
        dp_new[s | keyto] = min(d + price, dp_new[s | keyto])

    dp = dp_new
    # print(dp)

cost = dp[-1]
print(cost if cost != float("inf") else -1)
