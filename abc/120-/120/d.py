class UnionFindTree:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def unite(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 > d2:
            self.table[r1] = r2
            self.table[r2] += d1
        else:
            self.table[r2] = r1
            self.table[r1] += d2


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))
edges.reverse()
score = []
score.append(n * (n - 1) // 2)

uft = UnionFindTree(n)

for (a, b) in edges[:-1]:
    if uft.find(a, b):
        score.append(score[-1])
        continue

    root_a = uft.table[uft._root(a)]
    root_b = uft.table[uft._root(b)]
    score.append(score[-1] - root_a * root_b)
    uft.unite(a, b)

score.reverse()
print("\n".join(map(str, score)))
