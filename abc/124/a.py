a, b = list(map(int, input().split()))
answer = []
if a > b:
    answer.append(a)
    a -= 1
else:
    answer.append(b)
    b -= 1
answer.append(max(a, b))
print(sum(answer))
