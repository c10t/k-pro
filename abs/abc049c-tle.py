# -*- coding: utf-8 -*-

# ABC049C - Daydream


def main():
    # |s| in [1, 10 ** 5]
    s = input()
    t = ''
    addlist = ['dream', 'dreamer', 'erase', 'eraser']

    for i in range(len(s)):
        for x in addlist:
            if s[-i-1:] == x + t:
                t = x + t

    if s == t:
        print('YES')
    else:
        print('NO')


main()
