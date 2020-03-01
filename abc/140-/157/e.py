n = int(input())
s = input()
q = int(input())

query = []

for _ in range(q):
    x, y, z = input().split()

    if x == "1":
        query.append((x, int(y), z))
    else:
        query.append((x, int(y), int(z)))
