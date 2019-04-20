# -*- coding: utf-8 -*-

# ABC085C - Otoshidama


def main():
    # N in [1, 2000]
    # Y in [1000, 2 * (10 ** 7)]
    # Y = 1000m
    n, y = map(int, input().split())

    a, b, c = (-1, -1, -1)
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if 10000*i + 5000*j + 1000*k == y:
                a, b, c = i, j, k
                break

    print('{} {} {}'.format(a, b, c))


main()
