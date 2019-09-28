def main():
    n = int(input())
    hs = list(map(int, input().split()))

    for i in range(n - 1):
        if hs[i] < hs[i + 1]:
            hs[i + 1] -= 1

    answer = 'Yes'
    for i in range(n - 1):
        if hs[i] > hs[i + 1]:
            answer = 'No'
            break

    print(answer)


main()
