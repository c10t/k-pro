import numpy as np

n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a = np.sort(a)
f = np.sort(f)[::-1]


def ok(x):
    return np.clip(a - x // f, 0, None).sum() <= k


l, r = 0, 10 ** 12

while l <= r:
    mid = (l + r) // 2
    if ok(mid):
        r = mid - 1
    else:
        l = mid + 1

print(l)
