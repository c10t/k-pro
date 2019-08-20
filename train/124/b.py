n = int(input())
h = list(map(int, input().split()))

highest_before = 0
score = 0

for i in range(n):
    if h[i] >= highest_before:
        score += 1
    highest_before = max(h[i], highest_before)

print(score)
