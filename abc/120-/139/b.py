a, b = list(map(int, input().split()))

rest = b
count = 0
while rest > 1:
    rest -= a - 1
    count += 1

print(count)
