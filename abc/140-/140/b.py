n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

score = 0
prev = -1
for ai in a:
    score += b[ai - 1]
    if prev + 1 == ai:
        score += c[prev - 1]

    prev = ai

print(score)
