def main():
    n, x = list(map(int, input().split()))
    ls = list(map(int, input().split()))

    count = 1
    d = 0
    for i in range(n):
        d = d + ls[i]
        if d > x:
            break
        else:
            count += 1

    print(count)


main()
