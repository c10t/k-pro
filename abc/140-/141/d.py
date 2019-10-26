from heapq import heappush, heappop, heapify

n, m = list(map(int, input().split()))
q = list(map(lambda x: -int(x), input().split()))
heapify(q)

for _ in range(m):
    highest = -heappop(q)
    heappush(q, -(highest // 2))

cost = -sum(q)

print(cost)
