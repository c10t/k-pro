# from itertools import combinations

MOD = 10 ** 9 + 7

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)

if k > 1:
    score = 0
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            print(i, j)
else:
    print(0)
