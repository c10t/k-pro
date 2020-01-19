a, b = list(map(int, input().split()))

s1 = str(a) * b
s2 = str(b) * a

print(s1 if s1 < s2 else s2)
