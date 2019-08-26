from fractions import gcd

a, b, k = list(map(int, input().split()))
count = 1
for i in range(gcd(a, b), 0, -1):
    if a % i != 0 or b % i != 0:
        continue
    else:
        if count == k:
            print(i)
            break
        else:
            count += 1
