import math

n = int(input())
xs = []
for _ in range(5):
    xs.append(int(input()))


# TLE
def sim(n, xs):
    state = [n] + [0] * 5
    step = 0
    while state[5] < n:
        moves = [min(state[i], xs[i]) for i in range(5)]
        for i in range(5):
            state[i] -= moves[i]
            state[i + 1] += moves[i]
        step += 1

    return step


def solve(n, xs):
    return math.ceil(n / min(xs)) + 4


print(solve(n, xs))
