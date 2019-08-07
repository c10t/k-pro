def main():
    w, h, x, y = list(map(int, input().split()))
    print(w * h / 2, 1 if x == (w / 2) and y == (h / 2) else 0)


main()
