from bisect import bisect_left


def main():
    n, k = list(map(int, input().split()))
    v = list(map(int, input().split()))

    score = 0
    for i in range(n + 1):
        for j in range(n - i + 1):
            if k < i + j:
                continue

            hands = v[:i] + v[n - j:]
            hands = sorted(hands)

            # throw away negative points
            p = min(bisect_left(hands, 0), k - i - j)

            score = max(score, sum(hands[p:]))

    print(score)


main()
