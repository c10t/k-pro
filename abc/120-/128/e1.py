from operator import itemgetter
from bisect import bisect_left


def main():
    n, q = list(map(int, input().split()))
    stops = []
    for _ in range(n):
        s, t, x = list(map(int, input().split()))
        stops.append((s, t, x))
    delay = []
    for i in range(q):
        delay.append(int(input()))

    stops = sorted(stops, key=itemgetter(2))
    delay = sorted(delay)

    result = [-1] * q
    skips = [-1] * q

    for s, t, x in stops:
        sx = bisect_left(delay, s - x)
        tx = bisect_left(delay, t - x)
        while sx < tx:
            if skips[sx] == -1:
                result[sx] = x
                skips[sx] = tx
                sx += 1
            else:
                sx = skips[sx]

    for r in result:
        print(r)


main()
