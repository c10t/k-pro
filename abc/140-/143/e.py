INF = float("inf")
n, m, l = list(map(int, input().split()))
edge1 = [[0 if i == j else INF for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge1[a - 1][b - 1] = c

# for row in edge1:
#     print(row)

q = int(input())
queries = []

for _ in range(q):
    s, t = map(int, input().split())
    if s < t:
        queries.append((s - 1, t - 1))
    else:
        queries.append((t - 1, s - 1))

# shortest paths by Warshall Floyd
for k in range(n):  # through
    for i in range(n):  # from
        for j in range(n):  # to
            edge1[i][j] = min(edge1[i][j], edge1[i][k] + edge1[k][j])

edge2 = [[0 if i == j else INF for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if edge1[i][j] <= l:
            edge2[i][j] = 1

# shortest costs by Warshall Floyd
for k in range(n):  # through
    for i in range(n):  # from
        for j in range(n):  # to
            edge2[i][j] = min(edge2[i][j], edge2[i][k] + edge2[k][j])

# for row in edge2:
#     print(row)

for (s, t) in queries:
    # print(s, t)
    # print(edge2[s][t])
    print(edge2[s][t] - 1 if edge2[s][t] < INF else -1)
