def main():
    n = int(input())
    aa = list(map(int, input().split()))

    pos = [0] * n
    neg = [0] * n

    pos[0] = aa[0]
    neg[0] = -aa[0]

    for i, a in enumerate(aa[1:-1], start=1):
        pos[i] = max(pos[i - 1] + a, neg[i - 1] - a)
        neg[i] = max(pos[i - 1] - a, neg[i - 1] + a)

    pos[n - 1] = pos[n - 2] + aa[n - 1]
    neg[n - 1] = neg[n - 2] - aa[n - 1]

    score = max(pos[n - 1], neg[n - 1])

    print(score)


main()
