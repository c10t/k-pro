import numpy as np


def isint(x):
    return np.equal(np.mod(x, 1), 0)


def main():
    n, d = list(map(int, input().split()))
    vecs = []
    for _ in range(n):
        vecs.append(list(map(int, input().split())))

    vecs = np.array(vecs)
    # print(vecs)
    v1 = np.tile(vecs, (1, n))
    v2 = np.tile(vecs.reshape(1, n * d), (n, 1))
    # print(v1)
    # print(v2)
    dists = v1 - v2
    # print(dists)
    dists = dists.reshape([-1, d])
    # print(dists)
    dists = np.linalg.norm(dists, axis=1)
    # print(dists)
    score = (np.count_nonzero(isint(dists)) - n) // 2
    print(score)


main()
