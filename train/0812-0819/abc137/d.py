from heapq import heappush, heappop
from operator import itemgetter


def main(n, m, works):
    backward = sorted(works, key=itemgetter(0), reverse=True)
    q = []
    score = 0
    for i in range(1, m + 1):
        while backward and backward[-1][0] <= i:
            a, b = backward.pop()
            heappush(q, -b)
            # print(q)
        if q:
            b = -heappop(q)
            score += b

    return score


n, m = list(map(int, input().split()))
works = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    works.append((a, b))

print(main(n, m, works))
