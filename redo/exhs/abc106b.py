def solve(n: int):
    count = 0
    for k in range(1, n + 1, 2):
        num_aliquot = len([1 for j in range(1, k + 1) if k % j == 0])
        if num_aliquot == 8:
            count += 1

    return count


N = int(input())  # 1 <= N <= 200

print(solve(N))
