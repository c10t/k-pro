def main():
    n = int(input())
    ps = list(map(int, input().split()))
    score = 0
    for i in range(1, n - 1):
        if ps[i - 1] < ps[i] < ps[i + 1]:
            score += 1
        elif ps[i - 1] > ps[i] > ps[i + 1]:
            score += 1

    print(score)


main()
