from operator import itemgetter


def main():
    n = int(input())

    rest = []
    for i in range(1, n + 1):
        s, p = input().split()
        p = int(p)
        rest.append((i, s, p))

    rest = sorted(rest, key=itemgetter(2), reverse=True)
    rest = sorted(rest, key=itemgetter(1))
    for i, _, _ in rest:
        print(i)


main()
