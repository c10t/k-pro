def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    r, score, partial_sum = 0, 0, 0

    for l in range(n):
        while partial_sum < k:
            if r >= n:
                break
            else:
                partial_sum += a[r]
                r += 1
        if partial_sum < k:
            break
        score += n - r + 1
        partial_sum -= a[l]

    print(score)


main()
