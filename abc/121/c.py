from operator import itemgetter

n, m = list(map(int, input().split()))
shops = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    shops.append((a, b))

shops = sorted(shops, key=itemgetter(0))
rest = m
cost = 0
for a, b in shops:
    if rest > b:
        cost += a * b
        rest -= b
    else:
        cost += a * rest
        break

print(cost)
