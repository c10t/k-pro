from fractions import gcd  # in math module python >= 3.5


def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) < 3:
        print(max(a))
        return

    ls = []
    for i in range(n+1):
        if i == 0:
            ls.append(0)
        else:
            ls.append(gcd(ls[i-1], a[i-1]))

    rs = []
    for i in range(n+1):
        if i == 0:
            rs.append(0)
        else:
            rs.append(gcd(rs[i-1], a[-i]))
    rs = list(reversed(rs)) + [0]

    m = [gcd(ls[i], rs[i+1]) for i in range(n+1)]

    print(max(m))


main()
