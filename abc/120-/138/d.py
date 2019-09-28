n, q = list(map(int, input().split()))
# NG: [set()] * n <- all points same set
edge = [set() for _ in range(n)]
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edge[a].add(b)
    edge[b].add(a)

opr = [0] * n
for _ in range(q):
    p, x = list(map(int, input().split()))
    p -= 1
    opr[p] += x

score = [-1] * n
q = [(0, 0)]
while q:
    # print(*q)
    node, w = q.pop()
    w += opr[node]
    score[node] = w
    # print(*score)
    for child in edge[node]:
        if score[child] == -1:
            q.append((child, w))

print(*score)
