
def count(s):
    w = s.count('.')
    candidate = w
    for i in range(len(s)):
        if s[i] == '#':
            w += 1
        else:
            w -= 1
        candidate = min(candidate, w)

    return candidate


def main():
    _ = int(input())
    s = input()  # '#.#' -> '###'

    print(count(s))


main()
