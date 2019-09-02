import numpy as np

n, m = map(int, input().split())

tastes = np.zeros((n, m), dtype=np.int8)
for i in range(n):
    ka = list(map(int, input().split()))
    for j in range(ka[0]):
        # print(i, ka[j + 1] - 1)
        tastes[i][ka[j + 1] - 1] = 1

    # for t in tastes:
    #     print(t)
    # print("---")

# tastes = np.array(tastes)
# print(tastes)

# count_nonzero has no axis option for old numpy ( < 1.12.0 )
score = np.sum(np.sum(tastes == 1, axis=0) == n)
print(score)
