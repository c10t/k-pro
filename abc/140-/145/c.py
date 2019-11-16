from itertools import permutations, combinations
from math import sqrt, factorial

n = int(input())
d = []
for _ in range(n):
    x, y = map(int, input().split())
    d.append((x, y))

l = [[0 for _ in range(n)] for _ in range(n)]
# print(d)
# print(l)

for i, j in combinations(range(n), 2):
    # print("comb:", i, j)
    dist = (d[i][0] - d[j][0]) ** 2 + (d[i][1] - d[j][1]) ** 2
    dist = sqrt(dist)
    # print(dist)
    # print(i, j)
    l[i][j] = dist
    l[j][i] = dist


# print(l)

s = 0
for p in permutations(range(n)):
    # print(p)
    for k in range(len(p) - 1):
        s += l[p[k]][p[k + 1]]

print(s / factorial(n))
