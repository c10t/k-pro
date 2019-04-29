def main():
    a, b, t = list(map(int, input().split()))
    i = a
    count = 0
    while i < t + 0.5:
        count += b
        i += a

    print(count)


main()
