# from scipy.special import comb
# from math import factorial
# from operator import mul
# from functools import reduce

# def combination(n, r):
#     r = min(n - r, r)
#     if r == 0:
#         return 1
#     over = reduce(mul, range(n, n - r, -1))
#     under = reduce(mul, range(1, r + 1))
#     return over // under


def combination(n, r, mod=10 ** 9 + 7):
    n1, r = n + 1, min(r, n - r)
    numerator = denominator = 1
    for i in range(1, r + 1):
        numerator = numerator * (n1 - i) % mod
        denominator = denominator * i % mod

    return numerator * pow(denominator, mod - 2, mod) % mod


x, y = map(int, input().split())

if (x + y) % 3 != 0 or (x > 2 * y or y > 2 * x):
    print(0)
else:
    # (+1, +2) n
    # (+2, +1) m
    # n + 2m = x
    # 2n + m = y
    m = (2 * x - y) // 3
    n = (2 * y - x) // 3
    # score = factorial(n + m) // factorial(n) // factorial(m)
    # score = comb(n + m, n, exact=True)
    score = combination(n + m, n)
    print(score)
