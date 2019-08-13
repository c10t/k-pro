def main(n, a):
    x = [0] * n
    # print(a)
    # print(a[1:-1:2])
    x[0] = sum(a) - 2 * sum(a[1:-1:2])
    for i in range(n - 1):
        x[i + 1] = 2 * a[i] - x[i]
    return ' '.join([str(xi) for xi in x])


N = int(input())
A = list(map(int, input().split()))
print(main(N, A))
# print(main(3, [2, 2, 4]))
