

def main():
    _ = int(input())
    s = input()
    k = int(input())
    ans = ''
    r = s[k - 1]
    for char in s:
        if char == r:
            ans += char
        else:
            ans += '*'

    print(ans)


main()
