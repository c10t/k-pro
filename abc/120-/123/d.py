# from heapq import heappush, heappop

X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
C = sorted(C, reverse=True)


def solve1():
    ab = sorted([x + y for x in A[:K] for y in B[:K]], reverse=True)
    f = sorted([c + e for c in C for e in ab[:K]], reverse=True)
    return f[:K]


def solve2():
    pass


for top in solve1():
    print(top)
