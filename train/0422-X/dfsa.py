
# https://atc001.contest.atcoder.jp/tasks/dfs_a

# https://teratail.com/questions/139765
import sys
sys.setrecursionlimit(10 ** 6)


def main():
    h, w = list(map(int, input().split()))
    c = []
    for _ in range(h):
        c.append([char for char in input()])

    start = (0, 0)
    goal = (0, 0)
    for i, row in enumerate(c):
        for j, item in enumerate(row):
            if item == 's':
                start = (i, j)
            if item == 'g':
                goal = (i, j)

    reached = [[False for _ in range(w)] for _ in range(h)]
    # print(c)
    # print(start)
    # print(goal)

    def search(x, y):
        # print(x, y)
        if x < 0 or x > w - 1 or y < 0 or y > h - 1:
            return
        if c[y][x] == '#':
            return
        if reached[y][x]:
            return

        reached[y][x] = True

        search(x + 1, y)
        search(x - 1, y)
        search(x, y + 1)
        search(x, y - 1)

    search(start[0], start[1])
    print('Yes' if reached[goal[0]][goal[1]] else 'No')


main()
