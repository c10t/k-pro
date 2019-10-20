import sys
import numpy as np

from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m, l = map(int, readline().split())
rest = np.array(read().split(), np.int64)
abc = rest[: m + m + m]
a = abc[::3]
b = abc[1::3]
c = abc[2::3]
st = rest[m + m + m + 1 :]
s = st[::2]
t = st[1::2]


dist_graph = csr_matrix((c, (a, b)), (n + 1, n + 1))
dist_path = floyd_warshall(dist_graph, directed=False)

cost_graph = np.full((n + 1, n + 1), np.inf)
np.fill_diagonal(cost_graph, 0)
cost_graph[dist_path <= l] = 1

cost_path = floyd_warshall(cost_graph, directed=False)

cost_path[cost_path == np.inf] = 0
cost_path = (cost_path).astype(int)

x = cost_path[s, t] - 1

print("\n".join(x.astype(str)))
