import numpy as np


def main():
    h, w = list(map(int, input().split()))
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    grid = np.array(grid) == '.'
    # print(grid)

    L = np.zeros((h, w), dtype=int)
    R = np.zeros((h, w), dtype=int)
    D = np.zeros((h, w), dtype=int)
    U = np.zeros((h, w), dtype=int)

    for i in range(1, h):
        U[i] = (U[i - 1] + 1) * grid[i - 1]
        # print(U[i])
    # print(U)

    for i in reversed(range(h - 1)):
        D[i] = (D[i + 1] + 1) * grid[i + 1]

    for j in range(1, w):
        L[:, j] = (L[:, j - 1] + 1) * grid[:, j - 1]
        # print(L[:, j])
    # print(L)

    for j in reversed(range(w - 1)):
        R[:, j] = (R[:, j + 1] + 1) * grid[:, j + 1]

    score = ((U + D + L + R) * grid).max() + 1
    print(score)


main()
