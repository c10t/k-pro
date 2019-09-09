a, b = list(map(int, input().split()))


def f(x):
    rem = [x, x ^ (x - 1), x ^ (x - 1) ^ (x - 2), 0]
    return rem[x % 4]


print(f(b) ^ f(a - 1))
