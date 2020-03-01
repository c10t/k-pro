a = []

for _ in range(3):
    a.append(list(map(int, input().split())))

n = int(input())

b = []
for _ in range(n):
    b.append(int(input()))

patterns = (
    [[a[i][i] for i in range(3)], [a[2 - i][i] for i in range(3)]]
    + [[a[0][i], a[1][i], a[2][i]] for i in range(3)]
    + [[a[i][0], a[i][1], a[i][2]] for i in range(3)]
)

answer = "No"
for a0, a1, a2 in patterns:
    if a0 in b and a1 in b and a2 in b:
        answer = "Yes"
        break

print(answer)
