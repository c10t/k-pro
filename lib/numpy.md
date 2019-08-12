# numpy note

使ったら残しておく

## ABC133 B

```python
def isint(x):
    return np.equal(np.mod(x, 1), 0)


def main():
    n, d = list(map(int, input().split()))
    vecs = []
    for _ in range(n):
        vecs.append(list(map(int, input().split())))

    vecs = np.array(vecs)
    # [[ 1  2]
    #  [ 5  5]
    #  [-2  8]]
    v1 = np.tile(vecs, (1, n))
    v2 = np.tile(vecs.reshape(1, n * d), (n, 1))
    dists = v1 - v2
    # [[ 1  2  1  2  1  2]  - [[ 1  2  5  5 -2  8]
    #  [ 5  5  5  5  5  5]  -  [ 1  2  5  5 -2  8]
    #  [-2  8 -2  8 -2  8]] -  [ 1  2  5  5 -2  8]
    dists = dists.reshape([-1, d])  # -1: infer the dimension
    # [[ 0  0]
    #  [-4 -3]
    #  [ 3 -6]
    #  [ 4  3]
    #  [ 0  0]
    #  [ 7 -3]
    #  [-3  6]
    #  [-7  3]
    #  [ 0  0]]
    dists = np.linalg.norm(dists, axis=1)  # axis=1 row-wise norm
    # [0.  5.  6.70820393  5.  0.  7.61577311  6.70820393  7.61577311 0.  ]
    score = (np.count_nonzero(isint(dists)) - n) // 2  # remove itself and duplicates
    print(score)

main()
```

