def tokyoto(s):
    count = 0
    tokyoto = ['tokyo', 'kyoto']
    rest = s
    while len(rest) >= 5:
        # print(rest)
        if rest[-5:] in tokyoto:
            count += 1
            rest = rest[:-5]
        else:
            rest = rest[:-1] if len(rest) > 0 else ''
    return count


def main():
    t = int(input())
    s = []
    for _ in range(t):
        s.append(input())
    for item in s:
        print(tokyoto(item))


main()
