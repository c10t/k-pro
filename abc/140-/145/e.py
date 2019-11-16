from operator import itemgetter

n, t = map(int, input().split())
menu = []
for _ in range(n):
    a, b = map(int, input().split())
    menu.append((a, b))

m2 = sorted([x for x in menu if x[0] < t], key=lambda x: x[1] / x[0])  # , reverse=True
print(m2)
score = 0
rest = t
while rest > 0 and len(m2) > 0:
    minu = [x for x in m2 if x[0] < rest]
    if len(minu) > 0:
        a, b = minu.pop()
        m2.remove((a, b))
    else:
        a, b = m2.pop()
    print(a, b)

    if rest - a > 0:
        score += b
        rest -= a
        menu.remove((a, b))
    else:
        break

score += max(menu, key=itemgetter(1))[1] if len(menu) > 0 else 0

print(score)
