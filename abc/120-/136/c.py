# WA
def main():
    n = int(input())
    hs = list(map(int, input().split()))

    answer = 'Yes'
    for i in range(n - 2):
        if hs[i] - 1 > hs[i + 1]:
            answer = 'No'
            break

        if hs[i] > hs[i + 1] and hs[i + 1] > hs[i + 2]:
            answer = 'No'
            break

    print(answer)


main()
