# -*- coding: utf-8 -*-

# ABC088B - Card Game for Two


def main():
    _ = int(input().strip())  # in [1, 2, ..., 100]
    a = map(int, input().split())  # a_1 ... a_n in [1, 2, ..., 100]

    alice = 0
    bob = 0
    for i, v in enumerate(sorted(a, reverse=True)):
        if i % 2 == 0:
            alice += v
        else:
            bob += v

    print(alice - bob)


main()
