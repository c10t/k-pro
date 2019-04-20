# -*- coding: utf-8 -*-

# ABC085B - Kagami Mochi


def main():
    # N in [1, 100]
    # d_i in [1, 100]
    # 1 <= i <= N
    d = []
    n = int(input().strip())
    for k in range(n):
        d_k = int(input().strip())
        d.append(d_k)

    s = {d_k for d_k in d}

    print(len(s))


main()
