n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = 0
for i in range(n):
    r = b[i] - a[i]
    if r < 0:
        score += b[i]
    else:
        score += a[i]
        score += min(a[i + 1], r)
        a[i + 1] = max(0, a[i + 1] - r)

print(score)
