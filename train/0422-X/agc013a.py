
def splitter(n, a):
    count = 1
    mode = 'none'
    for i in range(1, n):
        if mode == 'incr':
            if a[-i-1] > a[-i]:
                # print('{} | {}'.format(a[-i-1], a[-i:]))
                count += 1
                # print('count:', count)
                mode = 'none'
            else:
                continue
        elif mode == 'decr':
            if a[-i-1] < a[-i]:
                # print('{} | {}'.format(a[-i-1], a[-i:]))
                count += 1
                # print('count:', count)
                mode = 'none'
        else:
            if a[-i-1] == a[-i]:
                # print('{} = {}'.format(a[-i-1], a[-i:]))
                continue
            elif a[-i-1] > a[-i]:
                # print('{} > {}'.format(a[-i-1], a[-i:]))
                mode = 'decr'
            elif a[-i-1] < a[-i]:
                # print('{} > {}'.format(a[-i-1], a[-i:]))
                mode = 'incr'
    return count


def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(splitter(n, a))


main()
