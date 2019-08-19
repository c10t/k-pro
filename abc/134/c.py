from operator import itemgetter

n = int(input())
a = []
for i in range(n):
    a.append((i, int(input())))

a = sorted(a, key=itemgetter(1))
for i in range(n):
    if i == a[-1][0]:
        maxx = a[-2][1]
    else:
        maxx = a[-1][1]
    print(maxx)
