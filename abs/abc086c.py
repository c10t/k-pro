# -*- coding: utf-8 -*-

# ABC086C - Traveling


def main():
    # N in [1, 10**5]

    n = int(input())
    p = []
    for _ in range(n):
        p.append(map(int, input().split()))

    plan = True
    t_c, x_c, y_c = 0, 0, 0
    for (t, x, y) in p:
        if abs(x - x_c) + abs(y - y_c) > t - t_c:
            plan = False
            break
        elif abs(x - x_c) + abs(y - y_c) == t - t_c:
            t_c, x_c, y_c = t, x, y
        else:
            d = abs(x - x_c) + abs(y - y_c)
            if d % 2 == (t - t_c) % 2:
                t_c, x_c, y_c = t, x, y
            else:
                plan = False
                break

    print('Yes' if plan else 'No')


main()
