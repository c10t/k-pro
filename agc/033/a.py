import sys
sys.setrecursionlimit(10 ** 6)


def main():
    h, w = list(map(int, input().split()))
    matrix = []
    for _ in range(h):
        matrix.append([c for c in input()])

    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def step(mat):
        filled = mat
        target = []
        for i in range(h):
            for j in range(w):
                if mat[i][j] == '#':
                    target.append((i, j))
        for ti, tj in target:
            for dy, dx in adj:
                if -1 < ti + dy < h and -1 < tj + dx < w:
                    filled[ti+dy][tj+dx] = '#'

        return filled

    def finished(mat):
        for i in range(h):
            for j in range(w):
                if mat[i][j] != '#':
                    return False
        return True

    count = 0
    mat = matrix
    for _ in range(h * w):
        # for line in mat:
        #    print(line)

        if finished(mat):
            break

        # print('-' * 20)
        mat = step(mat)
        count += 1

    print(count)


main()
