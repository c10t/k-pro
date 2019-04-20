# -*- coding: utf-8 -*-

# ABC081B - Shift only


def main():
    _ = int(input().strip())
    a = list(map(int, input().strip().split()))
    c = 0
    while c < 1024:
        if all([x % 2 == 0 for x in a]):
            c += 1
            a = list(map(lambda x: x // 2, a))
        else:
            break

    print(c)


main()
