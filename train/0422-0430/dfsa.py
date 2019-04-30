
# https://atc001.contest.atcoder.jp/tasks/dfs_a

# https://teratail.com/questions/139765
import sys
sys.setrecursionlimit(10 ** 6)


def main():
    h, w = list(map(int, input().split()))
    c = []
    for _ in range(h):
        c.append([char for char in input()])

    sx, sy = (0, 0)
    gx, gy = (0, 0)
    for i, row in enumerate(c):
        for j, item in enumerate(row):
            if item == 's':
                sx, sy = (i, j)
            if item == 'g':
                gx, gy = (i, j)

    reached = [[False for _ in range(w)] for _ in range(h)]

    def search(x, y):
        if x < 0 or x > h - 1 or y < 0 or y > w - 1:
            return
        if c[x][y] == '#':
            return
        if reached[x][y]:
            return

        reached[x][y] = True

        search(x + 1, y)
        search(x - 1, y)
        search(x, y + 1)
        search(x, y - 1)

    search(sx, sy)
    print('Yes' if reached[gx][gy] else 'No')


main()
