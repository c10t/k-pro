import numpy as np

H, W = list(map(int, input().split()))
h, w = list(map(int, input().split()))

mtx = np.ones([H, W])
# print(mtx)
mtx[:h] = 0
mtx[:, 0:w] = 0
# print(mtx)
print(np.count_nonzero(mtx))
