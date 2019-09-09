import numpy as np

N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

amtx = np.array(A)
bvec = np.array(B)
# amtx @ bvec.T > -C or np.matmul can't use ?
score = np.count_nonzero(np.dot(amtx, bvec.T) > -C)
print(score)
