n = int(input())
b = list(map(int, input().split()))
b.reverse()
score = 0
prev = 10 ** 9
for i in range(n - 1):
    score += min(b[i], prev)
    prev = b[i]
score += b[n - 2]
print(score)
