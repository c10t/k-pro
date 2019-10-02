n, k = list(map(int, input().split()))
s = input()

num_group = 1
for p1, p2 in zip(s, s[1:]):
    if p1 != p2:
        num_group += 1

score = min(n - 1, n - (num_group - 2 * k))

print(score)
