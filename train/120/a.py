a, b, c = list(map(int, input().split()))
q = b // a
answer = c if q >= c else q
print(answer)
