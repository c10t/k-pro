# -*- coding: utf-8 -*-

# ABC081A - Placing Marbles


def main():
    s = input().strip()
    c = [1 for si in s if si == '1']
    print(sum(c))


main()
