n = int(input())

answer = 0

if n % 2 == 0:
    answer = 0.5
else:
    answer = ((n // 2) + 1) / n

print(answer)
