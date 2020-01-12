from collections import defaultdict

n, m = list(map(int, input().split()))

submissions = []
for _ in range(m):
    num, result = input().split()
    submissions.append((int(num), result))

score = defaultdict(lambda: {"passed": False, "wa": 0})

for p, s in submissions:
    if score[p]["passed"]:
        pass
    elif s == "AC":
        score[p]["passed"] = True
    elif s == "WA":
        score[p]["wa"] += 1

ans = 0
pena = 0

# print(score)

for v in score.values():
    if v["passed"]:
        ans += 1
        pena += v["wa"]

print(ans, pena)
