# -*- coding: utf-8 -*-

# ABC083B - Some Sums


def main():
    # N in [1, 10**4]
    # A, B in [1, 36]
    # A <= B
    n, a, b = map(int, input().split())

    s = 0
    for k in range(1, n + 1):
        splitted = [int(i) for i in str(k)]
        ss = sum(splitted)
        if ss >= a and ss <= b:
            s += k

    print(s)


main()
