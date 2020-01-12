n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

score = max(0, n * m - sum(a))
score = -1 if score > k else score
print(score)
