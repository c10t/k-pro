def main():
    r, d, x = list(map(int, input().split()))

    past = x
    for _ in range(10):
        nx = r * past - d
        print(nx)
        past = nx


main()
