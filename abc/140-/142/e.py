from operator import itemgetter

n, m = list(map(int, input().split()))

keymap = [[0] * m for _ in range(n)]
prices = []
for j in range(m):
    a, b = list(map(int, input().split()))
    cs = list(map(int, input().split()))
    prices.append(a)
    for c in cs:
        keymap[c - 1][j] = 1

# print(keymap)
# print(prices)

costs = []
for i in range(n):
    ki = keymap[i]
    nonzeros = []
    for j in range(m):
        if ki[j] != 0:
            nonzeros.append((j, prices[j]))

    costs.append(min(nonzeros, key=itemgetter(1)) if len(nonzeros) > 0 else 0)

# print(costs)

keys = set()
if 0 in costs:
    print(-1)
else:
    goukei = 0
    for key, value in costs:
        if key not in keys:
            goukei += value
            keys.add(key)
    print(goukei)
