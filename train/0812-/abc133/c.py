def main(l, r):
    score = float('inf')

    for i in range(l, r):
        for j in range(i + 1, r + 1):
            current = i * j % 2019
            score = min(score, current)
            if score == 0:
                return score

    return score


L, R = list(map(int, input().split()))
print(main(L, R))
# print(main(2020, 2040))
