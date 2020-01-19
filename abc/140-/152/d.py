from collections import defaultdict


n = int(input())

count = defaultdict(int)

for x in map(str, range(1, n + 1)):
    head = x[0]
    tail = x[-1]
    count[(head, tail)] += 1

ans = 0
# if do not, RuntimeError: dictionary changed size during iteration
items = list(count.items())
for (head, tail), c in items:
    ans += c * count[(tail, head)]

print(ans)
