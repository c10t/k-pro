from collections import Counter
from itertools import accumulate

# from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

# for k in range(1, n + 1):
#     cx = deepcopy(c)

#     count = 0

#     while k <= len(cx):
#         # print(cx)
#         mc = cx.most_common()
#         for key, _ in mc[:k]:
#             cx[key] -= 1
#             if cx[key] < 1:
#                 del cx[key]
#         count += 1

#     print(count)

cv = Counter(c.values())
max_take = max(cv.keys())

lx = list(accumulate(cv[i] for i in range(max_take + 1)))
rx = list(accumulate(cv[i] * i for i in range(max_take + 1)))
ax = [rx[i] + (lx[-1] - lx[i]) * i for i in range(max_take + 1)]


def bisec(l0, r0, predicate):
    l, r = l0, r0

    while abs(l - r) > 1:
        mid = (l + r) // 2
        if predicate(mid):
            r = mid
        else:
            l = mid

    return r


for k in range(1, n + 1):
    print(bisec(n + 1, 0, lambda x: x * k <= ax[min(x, max_take)]))
