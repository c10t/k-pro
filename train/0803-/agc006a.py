def main():
    N = int(input())
    s = input()
    t = input()
    ans = 0
    for i in range(N):
        if s[i:] == t[:N - i]:
            break
        else:
            ans += 1
    print(N + ans)


main()
