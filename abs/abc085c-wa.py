# -*- coding: utf-8 -*-

# ABC085C - Otoshidama


def main():
    # N in [1, 2000]
    # Y in [1000, 2 * (10 ** 7)]
    # Y = 1000m
    n, y = map(int, input().split())

    a, b, c = (0, 0, 0)
    k = y // 1000

    nglist = [1, 2, 3, 5, 6, 7, 10, 11, 14, 15, 19, 20, 22, 23]

    m = k - n

    if m < 0:
        a, b, c = (-1, -1, -1)
    elif m == 0:
        a, b, c = (0, 0, n)
    elif m % 9 == 0:
        x = m // 9
        if x <= n:
            a, b, c = (x, 0, n - x)
        else:
            a, b, c = (-1, -1, -1)
    elif m % 4 == 0:
        x = m // 4
        if x <= n:
            a, b, c = (0, x, n - x)
        else:
            a, b, c = (-1, -1, -1)
    elif m in nglist:
        a, b, c = (-1, -1, -1)
    else:
        p = m % 4
        q = m // 4
        if p == 1:
            a, b, c = (1, q - 2, n - q + 1)
        elif p == 2:
            a, b, c = (2, q - 4, n - q + 2)
        elif p == 3:
            a, b, c = (3, q - 6, n - q + 3)

        if c < 0:
            a, b, c = (-1, -1, -1)

    print('{} {} {}'.format(a, b, c))


main()
