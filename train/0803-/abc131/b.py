def main():
    n, l = list(map(int, input().split()))
    a = [l + i for i in range(n)]
    if l < 0 and abs(l) >= n:
        score = sum(a[:n - 1])
    if l < 0 and abs(l) < n:
        score = sum(a)
    if l >= 0:
        score = sum(a[1:])
    print(score)


main()
