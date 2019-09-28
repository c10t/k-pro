from operator import itemgetter

n = int(input())
a = list(map(int, input().split()))

ax = [(i + 1, ai) for i, ai in enumerate(a)]
ax = sorted(ax, key=itemgetter(1))
an = [x[0] for x in ax]
print(*an)
