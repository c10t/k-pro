from collections import deque


def dfs(maze, start):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(0, start)])
    dist = [[-1] * w for _ in range(h)]

    depth, i, j = -1, -1, -1

    while q:
        depth, (i, j) = q.popleft()
        if dist[i][j] != -1:
            continue
        dist[i][j] = depth
        for di, dj in move:
            ni, nj = i + di, j + dj

            if (not 0 <= ni < h) or (not 0 <= nj < w):
                continue

            if maze[ni][nj] == "#" or dist[ni][nj] != -1:
                continue

            q.append((depth + 1, (ni, nj)))

    return depth, i, j


h, w = list(map(int, input().split()))

maze = []

for _ in range(h):
    maze.append(input())

answer = 0

for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            depth, i, j = dfs(maze, (i, j))
            answer = max(answer, depth)

print(answer)
