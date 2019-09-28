n = int(input())
hs = list(map(int, input().split()))

candidate = []
current = 0
for i in range(n - 1):
    if hs[i] >= hs[i + 1]:
        current += 1
    else:
        candidate.append(current)
        current = 0

candidate.append(current)

print(max(candidate))
