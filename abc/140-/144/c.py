n = int(input())


def solve(n):
    i = 1
    answer = n
    while i ** 2 <= n:
        q, r = divmod(n, i)
        if r == 0:
            answer = min(answer, i + q - 2)
        i += 1

    return answer


print(solve(n))
