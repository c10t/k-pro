def main():
    a, b, c = list(map(int, input().split()))
    d = a - b
    if d > c:
        remain = 0
    else:
        remain = c - d

    print(remain)


main()
