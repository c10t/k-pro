k, x = list(map(int, input().split()))
interval = [x + i for i in range(-k + 1, k)]
print(*interval)
