# -*- coding: utf-8 -*-

# ABC049C - Daydream


def main():
    # |s| in [1, 10 ** 5]
    s = input()
    t = ''
    addlist = ['dream', 'dreamer', 'erase', 'eraser']

    count = 0
    for i in range(len(s)):
        count += 1
        if count != 5 and count != 6 and count != 7:
            # print(s[-i-1:])
            continue
        for x in addlist:
            if s[-i-1:] == x + t:
                t = x + t
                count = 0
                # print(t)

    if s == t:
        print('YES')
    else:
        print('NO')


main()
