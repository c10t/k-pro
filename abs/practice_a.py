# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b, c = map(int, input().split())
    s = input()
    print("{} {}".format(a+b+c, s))


main()
