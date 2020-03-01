# from collections import defaultdict

n, m = list(map(int, input().split()))
# s = []
# c = []
# idx = 0


def solve(n, m):
    sc = dict()

    for _ in range(m):
        si, ci = list(map(int, input().split()))
        if si in sc.keys() and sc[si] != ci:
            return -1
        else:
            sc[si] = ci

    # print(sc)

    answer = ""
    for i in range(1, n + 1, 1):
        if i in sc.keys():
            if i == 1 and n > 1 and sc[i] == 0:
                return -1
            answer += str(sc[i])
        else:
            if i == 1 and n > 1:
                answer += "1"
            else:
                answer += "0"

    return answer


print(solve(n, m))
