from collections import Counter
from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

for k in range(1, n + 1):
    cx = deepcopy(c)

    count = 0

    while k <= len(cx):
        # print(cx)
        mc = cx.most_common()
        for key, _ in mc[:k]:
            cx[key] -= 1
            if cx[key] < 1:
                del cx[key]
        count += 1

    print(count)
