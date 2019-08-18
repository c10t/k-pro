from bisect import insort_left

n = int(input())
values = list(map(int, input().split()))
values = sorted(values)

for _ in range(n - 1):
    if len(values) < 2:
        break
    x = values.pop(0)
    y = values.pop(0)
    new_value = (x + y) / 2.0
    insort_left(values, new_value)

print(values[0])
