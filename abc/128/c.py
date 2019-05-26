from itertools import product


def main():
    n, m = list(map(int, input().split()))
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        ks = list(map(int, input().split()))
        _ = ks[0]
        s = ks[1:]
        for si in s:
            matrix[i][si - 1] = 1

    ps = list(map(int, input().split()))

    # print(f'n: {n}, m: {m}')
    # print(f'matrix: {matrix}')
    # print(f'p: {ps}')

    count = 0
    for case in product([0, 1], repeat=n):
        # print('------')
        # print(f'case: {case}')
        ok = 0
        for s, p in zip(matrix, ps):
            target = [
                1 for idx, si in enumerate(s) if si == 1 and case[idx] == 1
            ]
            # print(f'* s: {s}, case: {case}, target: {target}')
            if sum(target) % 2 == p:
                ok += 1
        # print(f'ok: {ok}')
        if ok == m:
            count += 1

    print(count)


main()
