def main():
    n, k = list(map(int, input().split()))
    s = input().strip()
    result = s[0:k - 1] + s[k - 1].lower() + (s[k:] if k < n else '')
    print(result)


main()
