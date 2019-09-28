def main():
    _ = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    u = [v - c for v, c in zip(v, c) if v - c > 0]
    print(sum(u))


main()
