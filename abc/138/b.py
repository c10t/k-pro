n = int(input())
a = list(map(int, input().split()))
answer = 1.0 / sum([1.0 / ai for ai in a])
print(answer)
