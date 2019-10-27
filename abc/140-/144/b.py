n = int(input())


def solve(n):
    if n < 10:
        return "Yes"
    for i in range(2, 10):
        q, r = divmod(n, i)
        # print(q, r)
        if q < 10 and r == 0:
            return "Yes"

    return "No"


print(solve(n))
