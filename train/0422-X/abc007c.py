def bfs(r, c, sy, sx, gy, gx, maze):
    queue = [(sx, sy, 0)]
    adjacents = [(0, 1, 1), (0, -1, 1), (1, 0, 1), (-1, 0, 1)]
    while (len(queue) > 0):
        y, x, depth = queue.pop(0)
        if x == gx and y == gy:
            return depth
        for dy, dx, dd in adjacents:
            next = (y + dy, x + dx, depth + dd)
            pt = maze[next[0] - 1][next[1] - 1]
            if 0 < next[0] <= r and 0 < next[1] <= c and pt == '.':
                maze[next[0] - 1][next[1] - 1] = 'x'
                queue.append(next)
    return 0


def main():
    r, c = list(map(int, input().split()))
    sy, sx = list(map(int, input().split()))
    gy, gx = list(map(int, input().split()))
    maze = []
    for _ in range(r):
        maze.append([char for char in input()])

    print('{}'.format(bfs(r, c, sy, sx, gy, gx, maze)))


main()
