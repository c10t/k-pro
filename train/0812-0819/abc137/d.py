import heapq
from operator import itemgetter


def main(n, m, jobs):
    backward = sorted(jobs, key=itemgetter(0), reverse=True)
    pass


n, m = list(map(int, input().split()))
jobs = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    jobs.append((a, b))

print(main(n, m, jobs))
