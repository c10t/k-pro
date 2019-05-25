def main():
    n, m = list(map(int, input().split()))
    lr = []
    for _ in range(m):
        l, r = list(map(int, input().split()))
        lr.append((l, r))

    lmax, rmin = lr[0]
    for l, r in lr:
        if l > lmax:
            lmax = l
        if r < rmin:
            rmin = r

    if lmax > rmin:
        print(0)
    else:
        print(rmin - lmax + 1)


main()
