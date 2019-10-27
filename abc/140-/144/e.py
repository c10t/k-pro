from heapq import heapify, heappop, heappush

n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

q = sorted([-ai for ai in a])
heapify(q)

for _ in range(k):
    max_cost = -heappop(q)
    if max_cost != 0:
        heappush(q, -(max_cost - 1))
    else:
        heappush(q, 0)

opt_a = sorted([-qi for qi in q])
opt_f = sorted(f, reverse=True)
print(opt_a[i] * opt_f[i] for i in range(n))
opt = max(opt_a[i] * opt_f[i] for i in range(n))

print(opt)
