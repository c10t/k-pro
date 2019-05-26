from operator import itemgetter


def main():
    n, q = list(map(int, input().split()))
    stops = []
    for _ in range(n):
        s, t, x = list(map(int, input().split()))
        stops.append((s, t, x))
    delay = []
    for i in range(q):
        delay.append([int(input()), False, -1])

    stops = sorted(stops, key=itemgetter(2))

    for s, t, x in stops:
        for idx, item in enumerate(delay):
            d, stopped, score = item
            if not stopped:
                time_at_x = x + d
                if s - 0.5 < time_at_x < t - 0.5:
                    delay[idx][2] = x
                    delay[idx][1] = True

    for item in delay:
        print(item[2])


main()
