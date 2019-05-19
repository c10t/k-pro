def main():
    n, k = list(map(int, input().split()))
    expect = 0
    for x in range(1, n + 1):
        if x > k - 1:
            expect += 1 / n
            continue
        n2w = 1
        for j in range(1, 100000):
            if x * (2**j) >= k:
                n2w = j
                break
        # print(f'n: {n} k: {k} x: {x} n2w: {n2w}')
        expect += (1 / n) * ((1 / 2) ** n2w)

    print(expect)


main()
