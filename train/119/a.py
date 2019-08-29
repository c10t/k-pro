s = input()


def solve(s):
    y, m, d = map(int, s.split("/"))
    if y < 2019:
        return "Heisei"
    if m < 5:
        return "Heisei"
    return "TBD"


print(solve(s))
