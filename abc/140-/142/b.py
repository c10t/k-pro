_, k = list(map(int, input().split()))
hs = list(map(int, input().split()))

print(len([h for h in hs if h >= k]))
