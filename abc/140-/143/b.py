from itertools import combinations

n = int(input())
d = list(map(int, input().split()))

print(sum(x * y for x, y in combinations(d, 2)))
