from bisect import bisect_left

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main(s, t):
    positions = {char: [] for char in ALPHABET}
    for i, char in enumerate(s):
        positions[char].append(i)

    current = 0
    answer = 0
    for char in t:
        pos_num = len(positions[char])
        if pos_num < 1:
            return -1
        idx = bisect_left(positions[char], current)
        if idx < pos_num:
            current = positions[char][idx] + 1
        else:
            answer += len(s)
            idx = bisect_left(positions[char], 0)
            current = positions[char][idx] + 1

    answer += current
    return answer


s = input()
t = input()
print(main(s, t))
