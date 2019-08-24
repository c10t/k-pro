n, q = list(map(int, input().split()))
s = input()
ls = []
for _ in range(q):
    l, r = list(map(int, input().split()))
    ls.append((l, r))

t = [0] * (n + 1)
for i in range(n):
    t[i + 1] = t[i] + (1 if s[i : i + 2] == "AC" else 0)

for (l, r) in ls:
    print(t[r - 1] - t[l - 1])
