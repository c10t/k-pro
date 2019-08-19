import sys

sys.setrecursionlimit(10 ** 5 + 5)

MOD = 10 ** 9 + 7


def dfs(current_node, parent_node, num_colors, graph):
    score = 1
    unavailable_colors = 0 if parent_node == -1 else 1
    for child_node in graph[current_node]:
        if child_node == parent_node:
            continue

        unavailable_colors += 1
        score = score * (num_colors - unavailable_colors) % MOD
        score = score * dfs(child_node, current_node, num_colors, graph) % MOD

    return score % MOD


N, K = list(map(int, input().split()))
G = [set() for _ in range(N)]
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)

print(dfs(0, -1, K, G) * K % MOD)
