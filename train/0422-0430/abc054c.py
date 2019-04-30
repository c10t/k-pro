from itertools import permutations


def calcpath(nodes, edges):
    start = nodes[0]
    pattern = permutations(nodes[1:])

    count = 0
    for p in pattern:
        path = [start] + list(p)
        for i in range(len(path) - 1):
            if edges[path[i]][path[i+1]] != 1:
                break
            if i + 1 == len(path) - 1:
                count += 1

    return count


def main():
    n, m = list(map(int, input().split()))
    nodes = [i for i in range(n)]
    edges = [[0 for i in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        edges[a - 1][b - 1] = 1
        edges[b - 1][a - 1] = 1
    print(calcpath(nodes, edges))


main()
