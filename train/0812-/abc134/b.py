n, d = list(map(int, input().split()))
score = n // (2 * d + 1) + (0 if n % (2 * d + 1) == 0 else 1)
# note: score = (n + 2 * d) // (2 * d + 1)
print(score)
