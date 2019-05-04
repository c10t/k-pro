# from copy import deepcopy
from time import perf_counter


def main():
    h, w = list(map(int, input().split()))
    matrix = []
    for _ in range(h):
        matrix.append([c for c in input()])

    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def step(q, m):
        next = []
        filled = m
        while len(q) > 0:
            y, x = q.pop(0)

            for dy, dx in adj:
                if -1 < y + dy < h and -1 < x + dx < w:
                    if m[y + dy][x + dx] == '.':
                        filled[y + dy][x + dx] = '#'
                        next.append((y + dy, x + dx))

        return next, filled

    iq = []
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#':
                iq.append((i, j))

    count = 0
    m = matrix
    while len(iq) > 0:
        # finished = all([m[i][j] == '#' for i in range(h) for j in range(w)])
        next, m = step(iq, m)
        if len(next) > 0:
            count += 1
            iq = next

    print(count)


st = perf_counter()
main()
ed = perf_counter()
print(ed - st)
