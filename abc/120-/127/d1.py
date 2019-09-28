from operator import itemgetter


def main():
    n, m = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b, c = list(map(int, input().split()))
        bc.append((b, c))

    xy = [(1, ai) for ai in alist] + bc
    rest = n
    total = 0
    for number, score in sorted(xy, key=itemgetter(1), reverse=True):
        if rest <= number:
            total += score * rest
            break
        else:
            total += score * number
            rest -= number

    print(total)


main()
