# from itertools import combinations
from bisect import bisect_left

n = int(input())
ls = list(map(int, input().split()))
ls.sort()

count = 0

# for a, b, c in combinations(ls, 3):
#     if a < b + c and b < c + a and c < a + b:
#         count += 1

# for j in range(n - 1, 1, -1):
#     last = ls[j]
#     for a, b in combinations(ls[:j], 2):
#         if a + b > last:
#             count += 1

for i in range(n - 1, 1, -1):
    for j in range(i - 1, 1, -1):
        idx = bisect_left(ls[:j], ls[i] - ls[j] + 1)
        if idx < j:
            count += j - idx

print(count)
