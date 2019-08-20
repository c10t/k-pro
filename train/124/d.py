from itertools import accumulate


def main(s, k, n):
    candidate = []
    prev = "1"
    count = 0
    for char in s:
        if prev == char:
            count += 1
        else:
            candidate.append(count)
            count = 1
        prev = char

    candidate.append(count)
    if prev == "0":
        candidate.append(0)

    w = 2 * k + 1
    if len(candidate) <= w:
        return len(s)

    acc = [0] + list(accumulate(candidate))
    score = 0
    for i in range(0, len(candidate) - w + 1, 2):
        score = max(score, acc[i + w] - acc[i])

    return score


n, k = list(map(int, input().split()))
s = input()

print(main(s, k, n))
