n, k, q = map(int, input().split())
a = []
for i in range(q):
    a.append(int(input()))

score = [k - q] * n
for ai in a:
    score[ai - 1] += 1

print("\n".join(map(lambda x: "Yes" if x > 0 else "No", score)))
