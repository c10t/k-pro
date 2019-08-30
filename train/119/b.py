n = int(input())

otc = []
for _ in range(n):
    x, u = input().split()
    otc.append((x, u))

score = 0
for x, u in otc:
    if u == "JPY":
        score += float(x)
    if u == "BTC":
        score += 380000 * float(x)

print(score)
