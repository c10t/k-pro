def main():
    _ = int(input())
    ds = list(map(int, input().split()))
    ds = sorted(ds)
    midpoint = len(ds) // 2
    if ds[midpoint] == ds[midpoint - 1]:
        score = 0
    else:
        score = ds[midpoint] - ds[midpoint - 1]

    print(score)


main()
