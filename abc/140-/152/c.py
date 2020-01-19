n = int(input())
ps = list(map(int, input().split()))

INF = 2 * 10 ** 5 + 1
ans = 0
min_p = INF
for i in range(n):
    if ps[i] <= min_p:
        ans += 1
        min_p = ps[i]

print(ans)
