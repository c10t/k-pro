from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 6)


def main():
    h, w = list(map(int, input().split()))
    matrix = []
    for _ in range(h):
        matrix.append([c for c in input()])

    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    depth = [[0 for _ in range(w)] for _ in range(h)]

    def calcdepth(i, j, current, m):
        checked = deepcopy(m)
        checked[i][j] = 'S'

        # for line in checked:
        #     print(line)
        # print('-' * 20)

        queue = [(i, j, 0)]
        while (len(queue) > 0):
            y, x, dep = queue.pop(0)
            if m[y][x] == '#':
                # print('hit!', dep)
                return dep

            for dy, dx in adj:
                next = (y + dy, x + dx, dep + 1)

                if -1 < next[0] < h and -1 < next[1] < w:
                    pt = checked[next[0]][next[1]]
                    if pt == '.':
                        checked[next[0]][next[1]] = 'X'
                        queue.append(next)
                    if pt == '#':
                        return dep + 1

        return 0

    for i in range(h):
        for j in range(w):
            depth[i][j] = calcdepth(i, j, 0, matrix)

    # for l in depth:
    #     print(l)

    print(max([depth[i][j] for i in range(h) for j in range(w)]))


main()
