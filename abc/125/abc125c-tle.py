from fractions import gcd  # in math module python >= 3.5
from functools import reduce


def gcdall(numlist):
    return reduce(gcd, numlist)


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    if len(a) < 3:
        print(max(a))
        return

    gcds = []
    for i in range(len(a)):

        excepted = [a[j] for j in range(len(a)) if j != i]
        b = 0
        while all([k % 2 == 0 for k in excepted]):
            b += 1
            excepted = [k // 2 for k in excepted]

        if b > 0:
            gcds.append(gcdall(excepted) * 2 * b)
        else:
            gcds.append(gcdall(excepted))

    print(max(gcds))


main()
