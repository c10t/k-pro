def main(s):
    pattern1 = ["0" if i % 2 == 0 else "1" for i in range(len(s))]
    pattern2 = ["1" if i % 2 == 0 else "0" for i in range(len(s))]
    dist1 = 0
    dist2 = 0
    for i in range(len(s)):
        if s[i] != pattern1[i]:
            dist1 += 1
        if s[i] != pattern2[i]:
            dist2 += 1

    return min(dist1, dist2)


s = input()
# s = "000"  # 1
# s = "10010010"  # 3
# s = "0"  # 0
print(main(s))
