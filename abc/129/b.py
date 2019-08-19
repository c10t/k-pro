def main():
    n = int(input())
    ws = list(map(int, input().split()))

    score = float('inf')
    for i in range(n):
        if i == 0:
            continue
        # print(ws[:i])
        current = abs(sum(ws[:i]) - sum(ws[i:]))
        if current < score:
            score = current

    print(score)


main()
