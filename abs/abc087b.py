# -*- coding: utf-8 -*-

# ABC087B - Coins


def main():
    a = int(input().strip())  # in [0, 1, ..., 50]
    b = int(input().strip())  # in [0, 1, ..., 50]
    c = int(input().strip())  # in [0, 1, ..., 50]
    x = int(input().strip())  # in [50, 100, 150, ..., 20000], x = 50y
    # a + b + c > 0
    # calc
    # |{ (n, m, k) | 500 * m + 100 * n + 50 * k = x }|

    coins = [(n, m, k)
             for n in range(a+1) for m in range(b+1) for k in range(c+1)]

    count = 0
    for (n, m, k) in coins:
        if 500 * n + 100 * m + 50 * k == x:
            count += 1

    print(count)


main()
