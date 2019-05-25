def main():
    a, b = list(map(int, input().split()))
    if a < 6:
        cost = 0
    elif 5 < a < 13:
        cost = b // 2
    else:
        cost = b
    print(cost)


main()
