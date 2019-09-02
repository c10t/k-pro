import sys
sys.setrecursionlimit(10 ** 5 + 5)

INF = 10 ** 9

N, A, B, C = list(map(int, input().split()))
L = []
for _ in range(N):
    l = int(input())
    L.append(l)


def dfs(current, a, b, c):
    if current == N:
        cost = abs(a - A) + abs(b - B) + abs(c - C) - 30
        return cost if min(a, b, c) > 0 else INF

    r0 = dfs(current + 1, a, b, c)
    r1 = dfs(current + 1, a + L[current], b, c) + 10
    r2 = dfs(current + 1, a, b + L[current], c) + 10
    r3 = dfs(current + 1, a, b, c + L[current]) + 10

    return min(r0, r1, r2, r3)


print(dfs(0, 0, 0, 0))
