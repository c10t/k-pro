n = int(input())
ps = list(map(int, input().split()))
pc = sorted(ps)
answer = "YES"
count = 0
for i in range(n):
    if ps[i] != pc[i]:
        count += 1
        if count > 2:
            answer = "NO"
            break

print(answer)
